class LineTranslationsController < ApplicationController
  before_action :set_line_translation, only: %i[ show edit update destroy ]

  def index

    @lines_pending_review_by_file = Hash.new
     FileTranslation.all.each do |f|
       @lines_pending_review_by_file[f.original_file.name] = f.line_translations.not_reviewed.first(5)
     end 

     @lines_review_by_file = Hash.new
     FileTranslation.all.each do |f|
       @lines_review_by_file[f.original_file.name] = f.line_translations.reviewed.last(5)
     end 

    @pending_line_translations = LineTranslation.not_reviewed.page(params[:page]).per(5)
    @reviewed_line_translations = LineTranslation.reviewed.page(params[:page]).per(5)
  end

  private

  def set_line_translation
    @line_translation = LineTranslation.find(params[:id])
  end
end