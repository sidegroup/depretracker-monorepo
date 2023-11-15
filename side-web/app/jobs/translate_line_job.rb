class TranslateLineJob < ApplicationJob
  queue_as :line_translations

  def perform(*args)
    # Do something later
  end
end
