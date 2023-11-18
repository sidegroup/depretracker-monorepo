class FileTranslation < ApplicationRecord
  # After create
  after_create :call_translation_job

  # Associations
  belongs_to :original_file, class_name: 'UserFile'
  belongs_to :source_language, class_name: 'Language'
  belongs_to :target_language, class_name: 'Language'
  has_many :line_translations, dependent: :destroy

  # Enums
  enum status: {
    'Pending' => 0,
    'In Progress' => 1,
    'Completed' => 2,
    'Failed' => 3
  }
  enum separators: { comma: ',', semicolon: ';' }

  # Validations
  validates_presence_of :original_file, :source_language, :target_language
  validates :status, presence: true, inclusion: { in: statuses.keys }
  validates :separator, presence: true, inclusion: { in: separators.values }, if: :target_columns?
  validate :target_range, if: :separator?

  def target_range
    unless target_columns.present?
      errors.add(:target_columns, "must be present")
      return
    end

    return if target_columns.all? { |column| column.to_i.between?(0, original_file.first_line.split(separator).size-1) }
    errors.add(:target_columns, "must be within range")
  end

  def call_translation_job
    FileTranslationJob.perform_later(self)
  end

  def finished_translation?
    line_translations.count == line_translations.translated.count
  end

  def notify
    return unless finished_translation?
    update(status: FileTranslation.statuses[:'Completed'])
  end

  def progress
    return 0 if line_translations.empty?
    line_translations.translated.count.to_f / line_translations.count.to_f * 100
  end

end
