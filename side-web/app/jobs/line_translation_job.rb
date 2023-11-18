class LineTranslationJob < ApplicationJob
  queue_as :line_translations

  def perform(*args)
    LineTranslationService.new(args.first).call
  end
end
