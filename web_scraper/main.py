import sys
from time import sleep
from src.crawlers.reddit_base_crawler import RedditBaseCrawler
from src.services.elasticsearch_service import ElasticSearchService
from src.factories.elastic_search_client import ElasticsearchClientFactory
from src.commands.create_csv import CreateCsv
from flask import Flask, request, send_file
from typing import *
import zipfile

#cria uma aplicação flask chamada "crawler"
app = Flask("crawler")

#cria uma rota para o endpoint "/crawl" que aceita apenas requisições do tipo POST
@app.route("/crawl", methods=["POST"])
def crawl():
    #obtem os dados enviados no corpo do formulário
    dados = request.form

    tipo: str = dados.get("tipo")
    client_id: str = dados.get("client_id")
    client_secret: str = dados.get("client_secret")
    username: str = dados.get("username")
    password: str = dados.get("password")
    user_agent: str = dados.get("user_agent")
    search_string = dados.get("search_string")

    # retira os espaços em branco e separa as palavras por vírgula
    subreddit = [word.strip() for word in dados.get("subreddits").split(",")]

    #cria um objeto do tipo RedditBaseCrawler
    crawler = RedditBaseCrawler(client_id, client_secret, username, password, user_agent, search_string, subreddit)

    #realizar o crawling
    crawler.crawl()

    # cria arquivo csv com as submissões
    CreateCsv().for_submissions(depressao.get_submission_index_name())
    # cria arquivo csv com os comentários
    CreateCsv().for_comments(depressao.get_comment_index_name())

    #cria um arquivo zip com os arquivos csv
    with zipfile.ZipFile('files.zip', 'w') as zipf:
    # Add multiple files to the zip
        zipf.write('output/{}.csv'.format(depressao.get_submission_index_name()))
        zipf.write('output/{}.csv'.format(depressao.get_comment_index_name()))

    #retorna o arquivo zip    
    return send_file('files.zip', mimetype='application/zip', as_attachment=True, download_name='depressivo.zip')


if __name__ == "__main__":
    #verifica se o serviço do ElasticSearch está pronto para iniciar a aplicação
    while not ElasticSearchService(
        ElasticsearchClientFactory.create()
    ).readiness_check():
        print("Waiting for Elasticsearch to be ready")
        sleep(5)
    
    #inicia a aplicação
    app.run(host='0.0.0.0')