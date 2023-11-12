require 'rails_helper'

RSpec.describe "file_translations/new", type: :view do
  before(:each) do
    assign(:file_translation, FileTranslation.new(
      user_file: nil
    ))
  end

  it "renders new file_translation form" do
    render

    assert_select "form[action=?][method=?]", file_translations_path, "post" do

      assert_select "input[name=?]", "file_translation[user_file_id]"
    end
  end
end
