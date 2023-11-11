class ReviewController < ApplicationController
  before_action :set_example, only: %i[ new create ]

  def new
    if @example.nil?
      flash[:notice] = "Todos as traduções foram revisados."
      redirect_to example_index_path
    end

    # @example.translation = TranslationService.call(@example.original,
    #                                                TranslationService::LANGUAGES[:english],
    #                                                TranslationService::LANGUAGES[:portuguese],
    #                                                TranslationService::Provider[:chatgpt])
  end

  def create
    if @example.update(example_params)
      @example.update!(reviewed: true)
      @next_example = Example.not_reviewed.first
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
    @example = Example.find(params[:example_id])
  end

  def example_params
    params.require(:example).permit(:approved)
  end

end
