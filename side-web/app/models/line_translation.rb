class LineTranslation < ApplicationRecord
  # After save
  after_create :enqueue_translation

  # Associations
  belongs_to :file_translation, class_name: 'FileTranslation'

  # Scopes
  scope :reviewed, -> { where(reviewed: true) }
  scope :not_reviewed, -> { where(reviewed: [nil, false]) }
  scope :translated, -> { where.not(translated_text: nil) }
  scope :not_translated, -> { where(translated_text: [nil, '']) }
  scope :with_error, -> { where("translated_text LIKE ?", "%Error%") }

  # Enums
  enum status: { pending: 0, approved: 1, rejected: 2 }
  enum separators: { comma: ',', semicolon: ';' }

  # Validations
  validates_presence_of :original_text
  validates_presence_of :batch_number
  validates_presence_of :separator, if: -> { targets? }
  validates :separator, inclusion: { in: separators.values }, if: :targets?
  validate :target_range, if: :separator?

  def target_range
    return if targets.all? { |target| target.to_i.between?(0, original_text.split(separator).size-1) }
    errors.add(:targets, "must be within range")
  end

  def enqueue_translation
    LineTranslationJob
      .set(wait: batch_number.minutes + 1.seconds)
      .perform_later(self)
  end

  def target_columns
    return [] unless targets?
    original_text.split(separator).values_at(*targets)
  end

  def reprocess
    update_column(:translated_text, nil)
    enqueue_translation
  end
end
