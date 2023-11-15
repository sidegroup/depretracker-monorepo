require 'rails_helper'

RSpec.describe FileTranslation, type: :model do
  it 'has a valid factory' do
    expect(build(:file_translation)).to be_valid
  end

  describe 'relations' do
    it { should belong_to(:original_file).class_name('UserFile') }
    it { should belong_to(:source_language).class_name('Language') }
    it { should belong_to(:target_language).class_name('Language') }
    it { should have_many(:line_translations).dependent(:destroy) }
  end

  describe 'validations' do
    it { should validate_presence_of(:original_file) }
    it { should validate_presence_of(:status) }
    it { should validate_presence_of(:source_language) }
    it { should validate_presence_of(:target_language) }

    context 'when separator is present' do
      subject { build(:file_translation, separator: separator, target_columns: target_columns) }
      let(:separator) { FileTranslation.separators[:comma] }

      context 'and target_columns are not present' do
        let(:target_columns) { nil }

        it { should_not be_valid }
      end

      context 'and target_columns are present' do
        context 'and target_columns are within range' do
          let(:target_columns) { ['0'] }

          it { should be_valid }
        end

        context 'and target_columns are above range' do
          let(:target_columns) { ['3'] }

          it { should_not be_valid }
        end
      end

    end

    context 'when target_columns are present' do
      subject { build(:file_translation, separator: separator, target_columns: target_columns) }
      let(:target_columns) { ['0'] }

      context 'and separator is not present' do
        let(:separator) { nil }

        it { should_not be_valid }
      end

      context 'and separator is present' do
        context 'and separator is valid' do
          let(:separator) { FileTranslation.separators[:comma] }

          it { should be_valid }
        end

        context 'and separator is invalid' do
          let(:separator) { 'invalid' }

          it { should_not be_valid }
        end
      end
    end
  end
end
