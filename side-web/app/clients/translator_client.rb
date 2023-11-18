class TranslatorClient
  def self.translate(source, target, text)
    HTTParty.get(url, query: { source: source, target: target, text: text }).parsed_response
  end

  private

  def self.url
    "http://translator/translate"
  end
end