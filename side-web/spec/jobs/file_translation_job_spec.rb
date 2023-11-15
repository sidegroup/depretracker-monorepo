require 'rails_helper'

RSpec.describe FileTranslationJob, type: :job do
  describe '#perform' do
    let(:file_translation) { build(:file_translation) }

    it 'calls FileTranslationService' do
      expect(FileTranslationService).to receive(:new)
                                          .with(file_translation)
                                          .and_return(FileTranslationService.new(file_translation))

      expect_any_instance_of(FileTranslationService).to receive(:call).and_return(true)

      FileTranslationJob.perform_now(file_translation)
    end
  end
end
