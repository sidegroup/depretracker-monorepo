from time import sleep
import sys
import os
from src.crawlers.reddit_base_crawler import RedditBaseCrawler
from src.services.elasticsearch_service import ElasticSearchService
from src.factories.elastic_search_client import ElasticsearchClientFactory
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS

from src.services.data_service import DataService
from src.controllers.data_controller import DataController, data_blueprint
from src.repositories.reddit_comment_repository import RedditCommentRepository
from src.repositories.reddit_submission_repository import RedditSubmissionRepository

#cria uma aplicação flask chamada "crawler"
app = Flask("crawler")
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

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
@app.route("/crawl", methods=["POST", "OPTIONS"])
def crawl():
    try:
        if request.method == "OPTIONS":
            return jsonify({"status": "ok"}), 200

        dados = request.get_json()

        required_fields = [
            "client_id", "client_secret", "username",
            "password", "user_agent", "search_string", "subreddits"
        ]
        for field in required_fields:
            if field not in dados or not dados[field]:
                return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400

        subreddits_str = dados["subreddits"].strip()
        subreddit = [word.strip() for word in subreddits_str.split(",") if word.strip()]
        if not subreddit:
            return jsonify({"error": "Nenhum subreddit válido fornecido"}), 400

        crawler = RedditBaseCrawler(
            dados["client_id"],
            dados["client_secret"],
            dados["username"],
            dados["password"],
            dados["user_agent"],
            dados["search_string"],
            subreddit,
            submission_repo,
            comment_repo
        )

        crawler.crawl()
        return jsonify({"message": "Crawling realizado com sucesso!"}), 200

    except Exception as e:
        return jsonify({"error": f"Erro durante o crawling: {str(e)}"}), 500

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

    app.run(host='0.0.0.0', port = 5000)