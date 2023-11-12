class CreateFileTranslations < ActiveRecord::Migration[7.0]
  def change
    create_table :file_translations do |t|
      t.references :original_file, null: false, foreign_key: { to_table: :user_files }

      t.timestamps
    end
  end
end
