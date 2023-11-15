class CreateFileTranslations < ActiveRecord::Migration[7.0]
  def change
    create_table :file_translations do |t|
      t.references :original_file, null: false, foreign_key: { to_table: :user_files }
      t.integer :status, default: 0
      t.references :source_language, null: false, foreign_key: { to_table: :languages }
      t.references :target_language, null: false, foreign_key: { to_table: :languages }
      t.string :target_columns, array: true, default: []
      t.string :separator

      t.timestamps
    end
  end
end
