class ExamplesController < ApplicationController
  before_action :set_example, only: %i[ show edit update destroy ]

  def index
    @pending_examples = Example.not_reviewed.order(:id)

    @reviewed_examples = Example.reviewed
  end

  def show
  end

  def new
    @example = Example.new
  end

  def edit
  end

  def create
    @example = Example.new(example_params)

    respond_to do |format|
      if @example.save
        format.html { redirect_to example_url(@example), notice: "Example was successfully created." }
        format.json { render :show, status: :created, location: @example }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @example.errors, status: :unprocessable_entity }
      end
    end
  end

  def update
    respond_to do |format|
      if @example.update(example_params)
        format.html { redirect_to example_url(@example), notice: "Example was successfully updated." }
        format.json { render :show, status: :ok, location: @example }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @example.errors, status: :unprocessable_entity }
      end
    end
  end

  def destroy
    @example.destroy

    respond_to do |format|
      format.html { redirect_to examples_url, notice: "Example was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  private
    def set_example
      @example = Example.find(params[:id])
    end

    def example_params
      params.require(:example).permit(:approved, :original, :translation)
    end
end
