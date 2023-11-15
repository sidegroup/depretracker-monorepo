class LineTranslationJob < ApplicationJob
  queue_as :line_translations

  def perform(*args)
    FileTranslationService.new(args.first).call
  end
end
