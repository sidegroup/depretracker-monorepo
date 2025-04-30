from elasticsearch import Elasticsearch

# Classe que cria um cliente para o ElasticSearch
class ElasticsearchClientFactory:
    @staticmethod
    def create():
        return Elasticsearch("http://host.docker.internal:9200")