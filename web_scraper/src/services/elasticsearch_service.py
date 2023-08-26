from elasticsearch import Elasticsearch

class ElasticSearchService:
    def __init__(self, es_client: Elasticsearch):
        self.es_client = es_client

    def readiness_check(self):
        return self.es_client.ping()