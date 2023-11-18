require 'rails_helper'

RSpec.describe LineTranslationJob, type: :job do
  describe '#perform' do
    let(:line_translation) { build(:line_translation) }

    it 'calls FileTranslationService' do
      expect(LineTranslationService).to receive(:new)
                                          .with(line_translation)
                                          .and_return(LineTranslationService.new(line_translation))

      expect_any_instance_of(LineTranslationService).to receive(:call).and_return(true)

      LineTranslationJob.perform_now(line_translation)
    end
  end
end
