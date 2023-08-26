from elasticsearch import Elasticsearch


class ElasticsearchClientFactory:
    @staticmethod
    def create():
        return Elasticsearch(hosts=[{'host': 'es', 'port': 9200, 'use_ssl': False}])