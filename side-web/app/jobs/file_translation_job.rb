class FileTranslationJob < ApplicationJob
  queue_as :file_translations

  def perform(*args)
    FileTranslationService.new(args.first).call
  end

end
