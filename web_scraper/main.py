import sys
from time import sleep
from src.crawlers.reddit_base_crawler import RedditBaseCrawler
from src.services.elasticsearch_service import ElasticSearchService
from src.factories.elastic_search_client import ElasticsearchClientFactory
from src.commands.create_csv import CreateCsv
from flask import Flask, request, send_file
from typing import *
import zipfile


app = Flask("crawler")

@app.route("/crawl", methods=["POST"])
def crawl():
    dados = request.form
    tipo: str = dados.get("tipo")
    client_id: str = dados.get("client_id")
    client_secret: str = dados.get("client_secret")
    username: str = dados.get("username")
    password: str = dados.get("password")
    user_agent: str = dados.get("user_agent")
    assunto: str = dados.get("assunto")
    search_string = dados.get("search_string")
    subreddit = [word.strip() for word in dados.get("subreddits").split(",")]

    crawler = RedditBaseCrawler(client_id, client_secret, username, password, user_agent, search_string, subreddit, assunto)

    crawler.crawl()

    # CreateCsv().for_submissions(depressao.get_submission_index_name())
    # CreateCsv().for_comments(depressao.get_comment_index_name())
    # with zipfile.ZipFile('files.zip', 'w') as zipf:
    # # Add multiple files to the zip
    #     zipf.write('output/{}.csv'.format(depressao.get_submission_index_name()))
    #     zipf.write('output/{}.csv'.format(depressao.get_comment_index_name()))
    #
    # return send_file('files.zip', mimetype='application/zip', as_attachment=True, download_name='depressivo.zip')


if __name__ == "__main__":
    while not ElasticSearchService(
        ElasticsearchClientFactory.create()
    ).readiness_check():
        print("Waiting for Elasticsearch to be ready")
        sleep(5)
        
    app.run(host='0.0.0.0')