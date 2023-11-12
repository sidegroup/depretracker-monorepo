class FileTranslation < ApplicationRecord
  # Associations
  belongs_to :original_file, class_name: 'UserFile'
  has_many :line_translations, dependent: :destroy

  # Enums
  enum status: [:pending, :reviewed]
  enum languages: {
    'English' => 0,
    'Spanish' => 1,
    'Portuguese' => 2,
  }
end
