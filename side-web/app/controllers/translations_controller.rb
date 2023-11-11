class TranslationsController < ApplicationController
  before_action :set_example, only: %i[ show edit update destroy ]

  def index
    @pending_translations = Translation.all

    @reviewed_translations = Translation.all
  end

  def show
  end

  def new
    @translation = Translation.new
  end

  def edit
  end

  def create
    @translation = Translation.new(example_params)

    respond_to do |format|
      if @translation.save
        format.html { redirect_to example_url(@translation), notice: "Example was successfully created." }
        format.json { render :show, status: :created, location: @translation }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @translation.errors, status: :unprocessable_entity }
      end
    end
  end

  def update
    respond_to do |format|
      if @translation.update(example_params)
        format.html { redirect_to example_url(@translation), notice: "Example was successfully updated." }
        format.json { render :show, status: :ok, location: @translation }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @translation.errors, status: :unprocessable_entity }
      end
    end
  end

  def destroy
    @translation.destroy

    respond_to do |format|
      format.html { redirect_to examples_url, notice: "Example was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    def set_example
      @translation = Translation.find(params[:id])
    end

    def example_params
      params.require(:translation).permit(:approved, :original, :translation)
    end
end
