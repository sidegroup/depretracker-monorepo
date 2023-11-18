# frozen_string_literal: true

require 'rails_helper'

RSpec.describe LineTranslationService, type: :service do
  subject { described_class.new(line_translation) }

  let!(:line_translation) do
    create(:line_translation,
           original_text: original_text.join(separator),
           translated_text: nil,
           separator: separator,
           targets: columns
    )
  end

  let(:first_target_column) { "My Text" }
  let(:first_translated_column) { "Meu Texto" }
  let(:last_target_column) { "My other text" }
  let(:last_translated_column) { "Meu outro texto" }

  let!(:original_text) { [ first_target_column, 1, "class", last_target_column ] }
  let!(:separator) { LineTranslation.separators[:comma] }

  describe '#call' do
    context 'when targeting multiple columns' do
      let(:columns) { [0, 3] }
      let(:expected_translated_text) { "Meu Texto,1,class,Meu outro texto" }

      before(:each) do
        allow(TranslatorClient).to receive(:translate).with("en", "pt", first_target_column).and_return(first_translated_column)
        allow(TranslatorClient).to receive(:translate).with("en", "pt", last_target_column).and_return(last_translated_column)
      end

      it 'translates the original_text' do
        expect { subject.call }.to change { line_translation.reload.translated_text }
                                     .from(nil)
                                     .to(expected_translated_text)
      end
    end

    context 'when target is massive' do
      let(:columns) { [0] }
      let(:first_target_column) { Faker::Lorem.paragraph(sentence_count: 100) }
      let(:first_translated_column) { Faker::Lorem.paragraph(sentence_count: 100) }
      let(:expected_translated_text) { [
        first_translated_column,
        1,
        "class",
        "My other text",
      ].join(separator) }

      before(:each) do
        allow(TranslatorClient).to receive(:translate).with("en", "pt", first_target_column).and_return(first_translated_column)
      end

      it 'translates the original_text' do
        expect { subject.call }.to change { line_translation.reload.translated_text }
                                     .from(nil)
                                     .to(expected_translated_text)
      end
    end

    context 'when targeting single columns' do
      before(:each) do
        allow(TranslatorClient).to receive(:translate).with("en", "pt", target_column).and_return(translated_column)
      end

      context 'first column' do
        let(:columns) { [0] }
        let(:expected_translated_text) { "Meu Texto,1,class,My other text" }
        let(:target_column) { first_target_column }
        let(:translated_column) { first_translated_column }

        it 'translates the original_text' do
          expect { subject.call }.to change { line_translation.reload.translated_text }
                                       .from(nil)
                                       .to(expected_translated_text)
        end
      end

      context 'last column' do
        let(:columns) { [3] }
        let(:expected_translated_text) { "My Text,1,class,Meu outro texto" }
        let(:target_column) { last_target_column }
        let(:translated_column) { last_translated_column }

        it 'translates the original_text' do
          expect { subject.call }.to change { line_translation.reload.translated_text }
                                       .from(nil)
                                       .to(expected_translated_text)
        end
      end
    end

  end
end
