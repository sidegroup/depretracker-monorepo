from time import sleep
import sys
import os
from src.crawlers.reddit_base_crawler import RedditBaseCrawler
from src.services.elasticsearch_service import ElasticSearchService
from src.factories.elastic_search_client import ElasticsearchClientFactory
from flask import Flask, request, send_file

from src.services.data_service import DataService
from src.controllers.data_controller import DataController, data_blueprint
from src.repositories.reddit_comment_repository import RedditCommentRepository
from src.repositories.reddit_submission_repository import RedditSubmissionRepository

#cria uma aplicação flask chamada "crawler"
app = Flask("crawler")

# cria cliente do elastic
es_client = ElasticsearchClientFactory.create()

# define os índices que serão usados na sua aplicação
assunto = ""
submission_repo = RedditSubmissionRepository(es_client, f"{assunto}posts")
comment_repo = RedditCommentRepository(es_client, f"{assunto}comments")

# Criação do serviço de dados
data_service = DataService(submission_repo, comment_repo)

# registra controller e blueprint
data_controller = DataController(data_service)

# Registra o blueprint no app
app.register_blueprint(data_blueprint)
#cria uma rota para o endpoint "/crawl" que aceita apenas requisições do tipo POST
@app.route("/crawl", methods=["POST"])
def crawl():
    try:
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
        crawler = RedditBaseCrawler(client_id, client_secret, username, password, user_agent, search_string, subreddit, submission_repo, comment_repo)
        #realizar o crawling
        crawler.crawl()
        return "Crawling iniciado com sucesso!", 200
    except Exception as e:
        return f"Erro durante o crawling: {str(e)}", 500


if __name__ == "__main__":
    elastic_service = ElasticSearchService(es_client)
    while True:
        try:
            if elastic_service.readiness_check():
                print("Elasticsearch está pronto!")
                break
        except Exception as e:
            print(f"Erro ao verificar Elasticsearch: {str(e)}")
        print("Aguardando Elasticsearch...")
        sleep(5)

    app.run(host='0.0.0.0')  # debug=False em produção!