class LineTranslation < ApplicationRecord
  # Associations
  belongs_to :file_translation

  # Scopes
  scope :not_reviewed, -> { where(reviewed: false) }
  scope :reviewed, -> { where(reviewed: true) }

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
end
