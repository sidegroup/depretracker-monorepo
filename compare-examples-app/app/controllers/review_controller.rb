class ReviewController < ApplicationController
  def index
    @examples = Example.not_reviewed

    @all_examples = Example.all
  end

  def new
    @example = Example.not_reviewed.last
  end
end
