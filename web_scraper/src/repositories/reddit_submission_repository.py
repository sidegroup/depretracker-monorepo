import datetime
from praw.models import Submission

# classe responsável por armazenar as submissões no Elasticsearch
class RedditSubmissionRepository:

    def __init__(self, es_client, target_index):
        self.es_client = es_client
        self.target_index = target_index

    # armazena uma submissão no Elasticsearch
    def store(self, submission: Submission):
        print(".", end="", flush=True)
        # cria um documento com os dados da submissão
        document = {
            "post_id": submission.id,  # id da submissão
            "author_name": submission.author.name if submission.author else None,
            "date": datetime.datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'), # converte a data para o formato 'YYYY-MM-DD HH:MM:SS'
            "title": submission.title,  # título da submissão
            "text": submission.selftext, # texto da submissão

        }
        resp = self.es_client.index(index=self.target_index, id=document["post_id"], document=document)
        return resp

    def list(self, page=1, page_size=10):
        from_ = (page - 1) * page_size
        query = {
            "from": from_,
            "size": page_size,
            "query": {
                "match_all": {}
            }
        }

        result = self.es_client.search(
            index=self.target_index,
            body=query
        )

        return {
            "data": [hit["_source"] for hit in result["hits"]["hits"]],
            "total": result["hits"]["total"]["value"]
        }

    def listAll(self, scroll='2m', batch_size=1000):
        query = {"query": {"match_all": {}}}

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

    def count(self):
        result = self.es_client.count(index=self.target_index)
        return result['count']
