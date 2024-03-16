# frozen_string_literal: true

class FileTranslationService
  include UserFilesHelper

  BATCH_SIZE = 60

  def initialize(file_translation)
    @file_translation = file_translation
  end

  def call
    @file_translation.update!(status: FileTranslation.statuses[:'In Progress'])

    lines.each_with_index do | line, index|
      batch = (index / BATCH_SIZE) + 1

      @file_translation.line_translations.create!(
        original_text: line,
        separator: @file_translation.separator,
        targets: @file_translation.target_columns,
        batch_number: batch
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

  def lines
    @lines ||= file_rows(@file_translation.original_file)
  end
end
