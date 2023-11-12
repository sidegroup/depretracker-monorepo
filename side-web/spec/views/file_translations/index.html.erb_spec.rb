require 'rails_helper'

RSpec.describe "file_translations/index", type: :view do
  before(:each) do
    assign(:file_translations, [
      FileTranslation.create!(
        user_file: nil
      ),
      FileTranslation.create!(
        user_file: nil
      )
    ])
  end

  it "renders a list of file_translations" do
    render
    cell_selector = Rails::VERSION::STRING >= '7' ? 'div>p' : 'tr>td'
    assert_select cell_selector, text: Regexp.new(nil.to_s), count: 2
  end
end
