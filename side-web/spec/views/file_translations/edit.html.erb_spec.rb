require 'rails_helper'

RSpec.describe "file_translations/edit", type: :view do
  let(:file_translation) {
    FileTranslation.create!(
      user_file: nil
    )
  }

  before(:each) do
    assign(:file_translation, file_translation)
  end

  it "renders the edit file_translation form" do
    render

    assert_select "form[action=?][method=?]", file_translation_path(file_translation), "post" do

      assert_select "input[name=?]", "file_translation[user_file_id]"
    end
  end
end
