from elasticsearch import Elasticsearch
from flask import current_app


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
        # Configura o índice para suportar grandes datasets

    def configure_index_settings(self, index_name: str, max_result_window: int = 50000):
        """Configura o limite máximo de resultados para paginação profunda"""
        try:
            body = {
                "index": {
                    "max_result_window": max_result_window
                }
            }
            self.es_client.indices.put_settings(index=index_name, body=body)
            return True
        except Exception as e:
            current_app.logger.error(f"Erro ao configurar índice {index_name}: {str(e)}")
            return False

        # Conta documentos em um índice

    def count_documents(self, index_name: str):
        """Retorna o número total de documentos em um índice"""
        try:
            result = self.es_client.count(index=index_name)
            return result['count']
        except Exception as e:
            current_app.logger.error(f"Erro ao contar documentos em {index_name}: {str(e)}")
            return 0

        # Busca paginada segura para grandes conjuntos de dados

    def safe_paginated_search(self, index_name: str, page: int, page_size: int, sort_field: str = "date"):
        """
        Busca paginada que usa search_after para páginas profundas
        além do limite padrão do Elasticsearch
        """
        # Calcular posição inicial
        start = (page - 1) * page_size

        # Usar search_after para páginas além de 10.000
        if start > 10000:
            return self.search_after_pagination(index_name, page, page_size, sort_field)

        # Para páginas iniciais, usar método tradicional
        try:
            query = {
                "query": {"match_all": {}},
                "from": start,
                "size": page_size,
                "sort": [{sort_field: {"order": "desc"}}]
            }
            response = self.es_client.search(index=index_name, body=query)
            return [hit["_source"] for hit in response["hits"]["hits"]]
        except Exception as e:
            current_app.logger.warning(f"Falha na busca direta: {str(e)}. Tentando search_after...")
            return self.search_after_pagination(index_name, page, page_size, sort_field)

        # Paginação com técnica search_after

    def search_after_pagination(self, index_name: str, page: int, page_size: int, sort_field: str):
        """Implementa paginação eficiente para resultados além de 10.000 registros"""
        try:
            # Obter ponto de partida (último documento da página anterior)
            last_sort_value = self.get_anchor_point(index_name, page, page_size, sort_field)
            if not last_sort_value:
                return []

            # Construir consulta search_after
            query = {
                "query": {"match_all": {}},
                "size": page_size,
                "sort": [{sort_field: {"order": "desc"}}],
                "search_after": last_sort_value
            }

            response = self.es_client.search(index=index_name, body=query)
            return [hit["_source"] for hit in response["hits"]["hits"]]
        except Exception as e:
            current_app.logger.error(f"Erro no search_after: {str(e)}")
            return []

        # Obtém ponto de ancoragem para search_after

    def get_anchor_point(self, index_name: str, page: int, page_size: int, sort_field: str):
        """Obtém o valor de ordenação para início da página solicitada"""
        try:
            # Calcular posição do último documento da página anterior
            prev_page_last_pos = (page - 1) * page_size - 1

            # Se estiver na primeira página, não há âncora
            if prev_page_last_pos < 0:
                return None

            query = {
                "query": {"match_all": {}},
                "size": 1,
                "from": prev_page_last_pos,
                "sort": [{sort_field: {"order": "desc"}}],
                "_source": False  # Não retorna os dados, apenas metadados
            }

            response = self.es_client.search(index=index_name, body=query)
            if not response["hits"]["hits"]:
                return None

            return response["hits"]["hits"][0]["sort"]
        except Exception as e:
            current_app.logger.error(f"Erro ao obter ponto de ancoragem: {str(e)}")
            return None

        # Streaming de documentos para grandes exportações

    def stream_all_documents(self, index_name: str, batch_size: int = 1000):
        """Gerador para streaming de todos os documentos (uso em exportações)"""
        try:
            query = {"query": {"match_all": {}}}
            scroll = "10m"  # Tempo de retenção do scroll

            # Inicia scroll
            response = self.es_client.search(
                index=index_name,
                scroll=scroll,
                size=batch_size,
                body=query
            )

            scroll_id = response["_scroll_id"]
            hits = response["hits"]["hits"]

            while hits:
                for hit in hits:
                    yield hit["_source"]

                # Próximo lote
                response = self.es_client.scroll(
                    scroll_id=scroll_id,
                    scroll=scroll
                )
                scroll_id = response["_scroll_id"]
                hits = response["hits"]["hits"]

            # Limpa recursos
            self.es_client.clear_scroll(scroll_id=scroll_id)
        except Exception as e:
            current_app.logger.error(f"Erro no streaming de documentos: {str(e)}")
            yield from []