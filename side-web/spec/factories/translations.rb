FactoryBot.define do
  factory :line_translation do
    original_text { "MyText" }

    trait :with_separator do
      separator { LineTranslation.separators.values.sample }
      targets { [1] }
    end
  end
end
