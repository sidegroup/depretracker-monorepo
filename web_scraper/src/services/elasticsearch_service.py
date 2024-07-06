from elasticsearch import Elasticsearch

class ElasticSearchService:
    def __init__(self, es_client: Elasticsearch):
        self.es_client = es_client

    def readiness_check(self):
        return self.es_client.ping()

    def create_index(self, index_name: str):
        return self.es_client.indices.create(index=index_name, ignore=400)

    def get_all_indices(self):
        return self.es_client.indices.get_alias("*")