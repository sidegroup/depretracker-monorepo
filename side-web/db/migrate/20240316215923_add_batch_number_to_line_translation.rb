class AddBatchNumberToLineTranslation < ActiveRecord::Migration[7.0]
  def change
    add_column :line_translations, :batch_number, :integer, null: false, default: 1
  end
end
