require 'rails_helper'

RSpec.describe FileTranslation, type: :model do
  it 'has a valid factory' do
    expect(build(:file_translation)).to be_valid
  end
end
