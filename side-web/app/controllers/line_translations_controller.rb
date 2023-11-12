class LineTranslationsController < ApplicationController
  before_action :set_example, only: %i[ show edit update destroy ]

  def index
    @pending_line_translations = LineTranslation.all

    @reviewed_line_translations = LineTranslation.all
  end

  def show
  end

  def new
    @line_translation = LineTranslation.new
  end

  def edit
  end

  def create
    @line_translation = LineTranslation.new(example_params)

    respond_to do |format|
      if @line_translation.save
        format.html { redirect_to example_url(@line_translation), notice: "Example was successfully created." }
        format.json { render :show, status: :created, location: @line_translation }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @line_translation.errors, status: :unprocessable_entity }
      end
    end
  end

  def update
    respond_to do |format|
      if @line_translation.update(example_params)
        format.html { redirect_to example_url(@line_translation), notice: "Example was successfully updated." }
        format.json { render :show, status: :ok, location: @line_translation }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @line_translation.errors, status: :unprocessable_entity }
      end
    end
  end

  def destroy
    @line_translation.destroy

    respond_to do |format|
      format.html { redirect_to examples_url, notice: "Example was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    def set_example
      @line_translation = LineTranslation.find(params[:id])
    end

    def example_params
      params.require(:line_translation).permit(:approved, :original, :line_translation)
    end
end
