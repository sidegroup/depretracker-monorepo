class CreateTranslations < ActiveRecord::Migration[7.0]
  def change
    create_table :translations do |t|
      t.boolean :approved
      t.text :original
      t.text :translated
      t.boolean :reviewed

      t.timestamps
    end
  end
end
