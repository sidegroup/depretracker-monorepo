FactoryBot.define do
  factory :file_translation do
    user_file { create(:user_file) }
  end
end
