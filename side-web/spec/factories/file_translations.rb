FactoryBot.define do
  factory :file_translation do
    original_file { create(:user_file) }
    source_language { create(:language) }
    target_language { create(:language) }
    target_columns { ['0'] }
    separator { FileTranslation.separators[:comma] }
  end
end
