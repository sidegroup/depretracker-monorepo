# frozen_string_literal: true

require 'rails_helper'

RSpec.describe FileTranslationService, type: :service do
  subject { described_class.new(file_translation) }

  let!(:file_translation) { build(:file_translation) }

  describe '#call' do
    context 'when file_translation is valid' do
      it 'creates line_translations' do
        expect { subject.call }.to change { LineTranslation.count }.by(2)
      end

      it 'updates file_translation status to in_progress' do
        expect { subject.call }.to change { file_translation.status }.from('Pending').to('In Progress')
      end
    end
  end

end
