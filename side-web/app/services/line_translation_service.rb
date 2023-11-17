# frozen_string_literal: true

class LineTranslationService
  def initialize(line_translation)
    @line_translation = line_translation
  end

  def call
    text_translation = TranslatorClient.translate(
      "auto",
      "pt",
      @line_translation.original_text
    )
  rescue StandardError => e

  end


end
