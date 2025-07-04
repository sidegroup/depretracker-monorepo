require 'rails_helper'

RSpec.describe LineTranslation, type: :model do
  it 'has a valid factory' do
    expect(build(:line_translation)).to be_valid
  end

  describe 'after creation' do
    let(:line_translation) { build(:line_translation) }

    it 'calls FileTranslationJob' do
      expect(LineTranslationJob).to receive(:set).with(wait: line_translation.batch_number.minutes + 1.seconds).and_return(LineTranslationJob)
      expect(LineTranslationJob).to receive(:perform_later).with(line_translation)
      line_translation.save
      line_translation.save
    end
  end

  describe 'associations' do
    it { should belong_to(:file_translation) }
  end

  describe 'validations' do
    it { should validate_presence_of(:original_text) }

    context 'when target is present' do
      subject { build(:line_translation, targets: [1, 2]) }

      it { should validate_presence_of(:separator) }
      it { should validate_presence_of(:batch_number) }
      it { is_expected.to validate_inclusion_of(:separator).in_array(LineTranslation.separators.values) }
      it 'should have a valid separator' do
        expect(build(:line_translation, targets: [0], separator: ',')).to be_valid
        expect(build(:line_translation, targets: [0], separator: ';')).to be_valid
        expect(build(:line_translation, targets: [0], separator: 'invalid')).to_not be_valid
      end
    end

    context 'when separator is present' do
      subject { build(:line_translation, separator: ',', targets: targets) }

      let(:targets) { nil }
      let(:separator) { LineTranslation.separators.values.sample }

      describe 'target range validation' do
        subject { build(:line_translation, separator: separator, targets: targets, original_text: original_text) }

        let(:original_text) { 'a,b,c' }
        let(:separator) { ',' }

        context 'when targets are within range' do
          let(:targets) { [1, 2] }

          it { should be_valid }
        end

        context 'when targets are above range' do
          let(:targets) { [3] }

          it { should_not be_valid }
        end

        context 'when targets are below range' do
          let(:targets) { [-1] }

          it { should_not be_valid }
        end
      end
    end
  end
end