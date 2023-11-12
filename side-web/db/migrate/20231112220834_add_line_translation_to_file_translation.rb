class AddLineTranslationToFileTranslation < ActiveRecord::Migration[7.0]
  def change
    add_reference :line_translations, :file_translation, null: false, foreign_key: true
  end
end
