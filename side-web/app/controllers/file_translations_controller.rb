class FileTranslationsController < ApplicationController
  before_action :set_file_translation, only: %i[ show edit update destroy ]
  before_action :set_user_file, except: %i[ index ]

  # GET /file_translations or /file_translations.json
  def index
    @file_translations = FileTranslation.all
  end

  # GET /file_translations/1 or /file_translations/1.json
  def show
  end

  # GET /file_translations/new
  def new
    @file_translation = FileTranslation.new
  end

  # POST /file_translations or /file_translations.json
  def create
    @file_translation = FileTranslation.new(
      file_translation_params.merge(
        separator: FileTranslation.separators[:comma],
        )
    )

    respond_to do |format|
      if @file_translation.save
        format.html { redirect_to file_translation_url(@file_translation), notice: "File translation was successfully created." }
        format.json { render :show, status: :created, location: @file_translation }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @file_translation.errors, status: :unprocessable_entity }
      end
    end
  end

  private
  def set_file_translation
    @file_translation = FileTranslation.find(params[:id])
  end

  def set_user_file
    @user_file = @file_translation.original_file if @file_translation
    @user_file = UserFile.find(params[:user_file_id]) if params[:user_file_id]
  end

  # Only allow a list of trusted parameters through.
  def file_translation_params
    params.require(:file_translation).permit(:original_file_id, :source_language_id, :target_language_id, target_columns: [])
  end
end
