# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2024_03_16_215923) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "active_storage_attachments", force: :cascade do |t|
    t.string "name", null: false
    t.string "record_type", null: false
    t.bigint "record_id", null: false
    t.bigint "blob_id", null: false
    t.datetime "created_at", null: false
    t.index ["blob_id"], name: "index_active_storage_attachments_on_blob_id"
    t.index ["record_type", "record_id", "name", "blob_id"], name: "index_active_storage_attachments_uniqueness", unique: true
  end

  create_table "active_storage_blobs", force: :cascade do |t|
    t.string "key", null: false
    t.string "filename", null: false
    t.string "content_type"
    t.text "metadata"
    t.string "service_name", null: false
    t.bigint "byte_size", null: false
    t.string "checksum"
    t.datetime "created_at", null: false
    t.index ["key"], name: "index_active_storage_blobs_on_key", unique: true
  end

  create_table "active_storage_variant_records", force: :cascade do |t|
    t.bigint "blob_id", null: false
    t.string "variation_digest", null: false
    t.index ["blob_id", "variation_digest"], name: "index_active_storage_variant_records_uniqueness", unique: true
  end

  create_table "file_translations", force: :cascade do |t|
    t.bigint "original_file_id", null: false
    t.integer "status", default: 0
    t.bigint "source_language_id", null: false
    t.bigint "target_language_id", null: false
    t.string "target_columns", default: [], array: true
    t.string "separator"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["original_file_id"], name: "index_file_translations_on_original_file_id"
    t.index ["source_language_id"], name: "index_file_translations_on_source_language_id"
    t.index ["target_language_id"], name: "index_file_translations_on_target_language_id"
  end

  create_table "languages", force: :cascade do |t|
    t.string "name", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "line_translations", force: :cascade do |t|
    t.boolean "approved"
    t.text "original_text"
    t.text "translated_text"
    t.boolean "reviewed"
    t.string "separator"
    t.string "targets", default: [], array: true
    t.bigint "file_translation_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.integer "batch_number", default: 1, null: false
    t.index ["file_translation_id"], name: "index_line_translations_on_file_translation_id"
  end

  create_table "user_files", force: :cascade do |t|
    t.string "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  add_foreign_key "active_storage_attachments", "active_storage_blobs", column: "blob_id"
  add_foreign_key "active_storage_variant_records", "active_storage_blobs", column: "blob_id"
  add_foreign_key "file_translations", "languages", column: "source_language_id"
  add_foreign_key "file_translations", "languages", column: "target_language_id"
  add_foreign_key "file_translations", "user_files", column: "original_file_id"
  add_foreign_key "line_translations", "file_translations"
end
