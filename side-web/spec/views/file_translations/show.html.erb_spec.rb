require 'rails_helper'

RSpec.describe "file_translations/show", type: :view do
  before(:each) do
    assign(:file_translation, FileTranslation.create!(
      user_file: nil
    ))
  end

  it "renders attributes in <p>" do
    render
    expect(rendered).to match(//)
  end
end
