json.extract! user_file, :id, :name, :attachment, :created_at, :updated_at
json.url user_file_url(user_file, format: :json)
json.attachment url_for(user_file.attachment)
