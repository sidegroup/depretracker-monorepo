FactoryBot.define do
  factory :user_file do
    attachment { Rack::Test::UploadedFile.new(Rails.root.join('spec', 'support', 'files', 'test.csv'), 'text/csv') }
  end
end
