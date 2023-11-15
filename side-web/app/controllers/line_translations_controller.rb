class LineTranslationsController < ApplicationController
  before_action :set_line_translation, only: %i[ show edit update destroy ]

  def index
    @pending_line_translations = LineTranslation.not_reviewed.first(5)

    @reviewed_line_translations = LineTranslation.reviewed.last(5)
  end
end
