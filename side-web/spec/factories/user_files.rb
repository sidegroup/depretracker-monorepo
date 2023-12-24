FactoryBot.define do
  factory :user_file do
    attachment { Rack::Test::UploadedFile.new(Rails.root.join('spec', 'support', 'files', 'test.csv'), 'text/csv') }

    trait :with_tsv do
      attachment { Rack::Test::UploadedFile.new(Rails.root.join('spec', 'support', 'files', 'test.tsv'), 'text/tab-separated-values') }
    end
  end
end
