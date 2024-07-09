class ReviewController < ApplicationController
  before_action :set_example, only: %i[ new create ]

  def new
    if @line_translation.nil?
      flash[:notice] = "Todos as traduções foram revisados."
      redirect_to example_index_path
    end

    # @example.translation = TranslationService.call(@example.original,
    #                                                TranslationService::LANGUAGES[:english],
    #                                                TranslationService::LANGUAGES[:portuguese],
    #                                                TranslationService::Provider[:chatgpt])
  end

  def create
    if @line_translation.update(example_params)
      @line_translation.update!(reviewed: true)
      file_translation = @line_translation.file_translation
      if file_translation.line_translations.count == LineTranslation.reviewedFileTranslation(file_translation).count
        file_translation.update!(status: FileTranslation.statuses[:'Completed'])

      end
       # == file_translation.line_translations.count ? file_translation.update!(status: FileTranslation.statuses[:'Completed']) : file_translation.update!(status: FileTranslation.statuses[:'In Progress'])
      @next_line = LineTranslation.not_reviewed.first
      flash[:notice] = "Tradução revisada com sucesso."
    else
      flash[:notice] = "Erro ao revisar tradução."
    end
    # @line_translation.file_translation.update!(status: FileTranslation.statuses[:'Completed'])
    if @next_line.nil?
      flash[:notice] = "Todos as traduções foram revisados."
      redirect_to line_translations_path
      return
    end

    redirect_to new_line_translation_review_path(@next_line)
  end

  private

  def set_example
    @line_translation = LineTranslation.find(params[:line_translation_id])
  end

  def example_params
    params.require(:line_translation).permit(:approved)
  end

end
