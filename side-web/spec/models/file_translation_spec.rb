require 'rails_helper'

RSpec.describe FileTranslation, type: :model do
  it 'has a valid factory' do
    expect(build(:file_translation)).to be_valid
  end

  describe 'relations' do
    it { should belong_to(:original_file).class_name('UserFile') }
    it { should have_many(:line_translations).dependent(:destroy) }
  end
end
