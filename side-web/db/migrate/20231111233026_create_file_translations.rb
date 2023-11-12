class CreateFileTranslations < ActiveRecord::Migration[7.0]
  def change
    create_table :file_translations do |t|
      t.references :user_file, null: false, foreign_key: true

      t.timestamps
    end
  end
end
