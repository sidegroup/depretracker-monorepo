class UserFile < ApplicationRecord
  has_one_attached :attachment

  has_many :file_translations, foreign_key: :original_file_id, dependent: :destroy

  def lines
    self.attachment.download.lines
  end

  def first_line
    self.attachment.download.lines.first
  end

  def second_to_n_line(n)
    self.attachment.download.lines.drop(1).first(n)
  end
end
