class LineTranslation < ApplicationRecord
  # After save
  after_save :enqueue_translation

  # Associations
  belongs_to :file_translation

  # Scopes
  scope :reviewed, -> { where(reviewed: true) }
  scope :not_reviewed, -> { where(reviewed: [nil, false]) }

  # Enums
  enum status: { pending: 0, approved: 1, rejected: 2 }
  enum separators: { comma: ',', semicolon: ';' }

  # Validations
  validates_presence_of :original_text
  validates_presence_of :separator, if: -> { targets? }
  validates :separator, inclusion: { in: separators.values }, if: :targets?
  validate :target_range, if: :separator?

  def target_range
    return if targets.all? { |target| target.to_i.between?(0, original_text.split(separator).size-1) }
    errors.add(:targets, "must be within range")
  end

  def enqueue_translation
    LineTranslationJob.perform_later(self)
  end

  def target_columns
    return [] unless targets?
    original_text.split(separator).values_at(*targets)
  end
end
