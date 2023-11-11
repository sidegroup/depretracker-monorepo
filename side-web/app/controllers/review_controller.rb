class ReviewController < ApplicationController
  before_action :set_example, only: %i[ new create ]

  def new
    if @translation.nil?
      flash[:notice] = "Todos as traduções foram revisados."
      redirect_to example_index_path
    end

    # @example.translation = TranslationService.call(@example.original,
    #                                                TranslationService::LANGUAGES[:english],
    #                                                TranslationService::LANGUAGES[:portuguese],
    #                                                TranslationService::Provider[:chatgpt])
  end

  def create
    if @translation.update(example_params)
      @translation.update!(reviewed: true)
      @next_example = Translation.not_reviewed.first
      flash[:notice] = "Tradução revisada com sucesso."
    else
      flash[:notice] = "Erro ao revisar tradução."
    end

    if @next_example.nil?
      flash[:notice] = "Todos as traduções foram revisados."
      redirect_to examples_path
      return
    end

    redirect_to new_example_review_path(@next_example)
  end

  private

  def set_example
    @translation = Translation.find(params[:example_id])
  end

  def example_params
    params.require(:translation).permit(:approved)
  end

end
