module UserFilesHelper
  def file_type(user_file)
    user_file.attachment.content_type
  end

  def file_header(user_file)
    clean_lines(user_file).first
  end

  def file_rows(user_file)
    clean_lines(user_file).drop(1)
  end

  private

  def file_delimiter(user_file)
    return ',' if is_csv?(user_file)
    return "\t" if is_tsv?(user_file)
  end

  def is_csv?(user_file)
    file_type(user_file) == 'text/csv'
  end

  def is_tsv?(user_file)
    file_type(user_file) == 'text/tab-separated-values'
  end

  def clean_lines(user_file)
    file_path = user_file.path
    delimiter = file_delimiter(user_file)
    lines = CSV.read(file_path, col_sep: delimiter)

    lines.map do |line|
      line.map do |cell|
        cell&.strip&.gsub("\n", ' ')
      end
    end
  end
end
