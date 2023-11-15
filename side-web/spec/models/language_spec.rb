require 'rails_helper'

RSpec.describe Language, type: :model do
  it 'has a valid factory' do
    expect(build(:language)).to be_valid
  end

  describe 'validations' do
    it { should validate_presence_of(:name) }
  end
end
