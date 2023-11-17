class TranslatorClient
  def self.ping
    response = HTTParty.get('http://translator/')
    response.parsed_response['ping']
  end

  def self.translate(source, target, text)
    HTTParty.get("http://translator/translate?source=#{source}&target=#{target}&text=#{text}")
  end
end