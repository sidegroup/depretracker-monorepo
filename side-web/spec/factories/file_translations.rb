FactoryBot.define do
  factory :file_translation do
    original_file { create(:user_file) }
  end
end
