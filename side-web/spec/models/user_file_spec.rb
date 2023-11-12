require 'rails_helper'

RSpec.describe UserFile, type: :model do
  it 'has a valid factory' do
    expect(build(:user_file)).to be_valid
  end

  describe 'associations' do
    it { should have_many(:file_translations).dependent(:destroy) }
  end
end
