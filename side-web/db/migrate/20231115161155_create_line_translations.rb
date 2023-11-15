class CreateLineTranslations < ActiveRecord::Migration[7.0]
  def change
    create_table :line_translations do |t|
      t.boolean :approved
      t.text :original_text
      t.text :translated_text
      t.boolean :reviewed
      t.string :separator
      t.string :targets, array: true, default: []
      t.references :file_translation, null: false, foreign_key: true

      t.timestamps
    end
  end
end
