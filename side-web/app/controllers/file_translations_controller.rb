class FileTranslationsController < ApplicationController
  before_action :set_file_translation, only: %i[ show edit update destroy retry download]
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
        format.html { redirect_to file_translation_url(@file_translation), notice: "Arquivo traduzido com sucesso." }
        format.json { render :show, status: :created, location: @file_translation }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @file_translation.errors, status: :unprocessable_entity }
      end
    end
  end

  def retry
    @file_translation.retry_failed_lines
  end

  def download
    csv = CSV.generate do |csv|
      @file_translation.line_translations.each do |translation|
        if translation.approved == true
          csv << [translation.translated_text]
        end
      end
    end

    csv_file = Tempfile.new('translation')
    csv_file.write(csv)
    csv_file.rewind
    csv_file.close

    send_file csv_file.path, type: 'text/csv', filename: translation_file_name
  end

  private
  def set_file_translation
    @file_translation = FileTranslation.find(params[:id])
  end

  def translation_file_name
    original_file = @file_translation.original_file.name.split('.').first
    target_language = @file_translation.target_language.name.downcase

    "#{original_file}_#{target_language}.csv"
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
