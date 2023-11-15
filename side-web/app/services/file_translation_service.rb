# frozen_string_literal: true

class FileTranslationService
  def initialize(file_translation)
    @file_translation = file_translation
  end

  def call
    @file_translation.update!(status: FileTranslation.statuses[:'In Progress'])
    @file_translation.original_file.lines.each do |line|
      @file_translation.line_translations.create!(
        original_text: line,
        separator: @file_translation.separator,
        targets: @file_translation.target_columns
      )
    end
  rescue StandardError => e
    @file_translation.update(status: FileTranslation.statuses[:'Failed'])
  end

  private

  def line_slit(line, separator)
    return line if separator.nil?

    line.split(separator)
  end
end
