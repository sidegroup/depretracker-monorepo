class LineTranslation < ApplicationRecord
  scope :not_reviewed, -> { where(reviewed: false) }
  scope :reviewed, -> { where(reviewed: true) }

  enum separators: { comma: ',', semicolon: ';' }

  validates_presence_of :original_text
  validates_presence_of :separator, if: -> { targets? }
  validates :separator, inclusion: { in: separators.values }, if: :targets?
  validate :target_range, if: :separator?

  def target_range
    return if targets.all? { |target| target.to_i.between?(0, original_text.split(separator).size-1) }
    errors.add(:targets, "must be within range")
  end
end
