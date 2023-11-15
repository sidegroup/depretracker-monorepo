class FileTranslation < ApplicationRecord
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

end
