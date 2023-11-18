# frozen_string_literal: true

class TranslatorController < ApplicationController

  def get
    render json: { translation: TranslatorClient.translate(params[:source], params[:target], params[:text]) }
  end
end
