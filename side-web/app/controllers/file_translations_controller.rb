class FileTranslationsController < ApplicationController
  before_action :set_file_translation, only: %i[ show edit update destroy ]

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

  # GET /file_translations/1/edit
  def edit
  end

  # POST /file_translations or /file_translations.json
  def create
    @file_translation = FileTranslation.new(file_translation_params)

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

  # PATCH/PUT /file_translations/1 or /file_translations/1.json
  def update
    respond_to do |format|
      if @file_translation.update(file_translation_params)
        format.html { redirect_to file_translation_url(@file_translation), notice: "File translation was successfully updated." }
        format.json { render :show, status: :ok, location: @file_translation }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @file_translation.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /file_translations/1 or /file_translations/1.json
  def destroy
    @file_translation.destroy

    respond_to do |format|
      format.html { redirect_to file_translations_url, notice: "File translation was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_file_translation
      @file_translation = FileTranslation.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def file_translation_params
      params.require(:file_translation).permit(:user_file_id)
    end
end
