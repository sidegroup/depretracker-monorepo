class CreateLineTranslations < ActiveRecord::Migration[7.0]
  def change
    create_table :line_translations do |t|
      t.boolean :approved
      t.text :original_text
      t.text :translated_text
      t.boolean :reviewed
      t.string :separator
      t.string :targets, array: true, default: []

      t.timestamps
    end
  end
end
