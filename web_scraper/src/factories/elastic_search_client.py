from elasticsearch import Elasticsearch

# Classe que cria um cliente para o ElasticSearch
class ElasticsearchClientFactory:
    @staticmethod
    def create():
        return Elasticsearch(hosts=[{'host': 'es', 'port': 9200, 'use_ssl': False}])