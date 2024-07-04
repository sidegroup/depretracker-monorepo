class LineTranslationsController < ApplicationController
  before_action :set_line_translation, only: %i[ show edit update destroy ]

  def index
    @pending_line_translations = LineTranslation.not_reviewed.page(params[:page]).per(5)
    @reviewed_line_translations = LineTranslation.reviewed.page(params[:page]).per(5)
  end

  private

  def set_line_translation
    @line_translation = LineTranslation.find(params[:id])
  end
end