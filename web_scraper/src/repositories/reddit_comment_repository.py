import datetime
from praw.models import Comment

# classe responsável por armazenar os comentários no Elasticsearch
class RedditCommentRepository:
    def __init__(self, es_client, target_index):
        self.es_client = es_client
        self.target_index = target_index

    def store(self, comment: Comment, post_id: int):
        print(".", end="", flush=True)
        # cria um documento com os dados do comentário
        document = {
            "id": comment.id, # id do comentário
            "author_id": comment.author.name if comment.author else None,
            "post_id": post_id,  # id do post ao qual o comentário pertence
            "body": comment.body, # corpo do comentário
            "date": datetime.datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'), # converte a data para o formato 'YYYY-MM-DD HH:MM:SS'
            "is_author_comment": comment.is_submitter,

        }
        # indexa o documento no Elasticsearch
        resp = self.es_client.index(index=self.target_index, id=document["id"], document=document)
        return resp

    def list(self, scroll='2m', batch_size=1000):
        query = {
            "query": {
                "match_all": {}
            }
        }

        # Inicia a busca com scroll
        result = self.es_client.search(
            index=self.target_index,
            body=query,
            scroll=scroll,
            size=batch_size
        )

        scroll_id = result["_scroll_id"]
        all_hits = result["hits"]["hits"]

        while True:
            result = self.es_client.scroll(scroll_id=scroll_id, scroll=scroll)
            hits = result["hits"]["hits"]
            if not hits:
                break
            all_hits.extend(hits)

        return all_hits

    def get_by_post_id(self, post_id: str):
        query = {
            "query": {
                "term": {
                    "post_id": post_id
                }
            }
        }

        resp = self.es_client.search(index=self.target_index, body=query, size=10000)
        return [hit["_source"] for hit in resp["hits"]["hits"]]

