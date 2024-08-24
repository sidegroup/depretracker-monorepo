from elasticsearch import Elasticsearch

# Classe que cria um cliente para o ElasticSearch
class ElasticSearchService:
    def __init__(self, es_client: Elasticsearch):
        self.es_client = es_client

    # verifica se o serviço do ElasticSearch está pronto
    def readiness_check(self):
        return self.es_client.ping()

    # cria um índice no ElasticSearch
    def create_index(self, index_name: str):
        return self.es_client.indices.create(index=index_name, ignore=400)

    # coleta todos os índices do ElasticSearch
    def get_all_indices(self):
        return self.es_client.indices.get_alias("*")