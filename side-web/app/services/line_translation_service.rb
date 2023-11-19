# frozen_string_literal: true

class LineTranslationService
  def initialize(line_translation)
    @line_translation = line_translation
  end

  def call
    @line_translation.translated_text = @line_translation.original_text

    target_columns.each do |index, column|
      translated_column = translate(column)

      @line_translation.translated_text = @line_translation.translated_text.gsub(column, translated_column)
    end

    @line_translation.save!
  rescue StandardError => e
    @line_translation.update(translated_text: "Error: #{e.message}")
  end

  private

  def translate(text)
    TranslatorClient.translate("en", "pt", text)
  end

  def target_columns
    targets.zip(columns.values_at(*targets)).to_h
  end

  def columns
    @line_translation.original_text.split(separator)
  end

  def targets
    @line_translation.targets.map(&:to_i)
  end

  def separator
    @line_translation.separator
  end
end
