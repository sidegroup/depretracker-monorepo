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
            "author_name": comment.author.name if comment.author else "", # se o autor for nulo, retorna uma string vazia
            "body": comment.body, # corpo do comentário
            "body_html": comment.body_html, # corpo do comentário em HTML
            "date": datetime.datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'), # converte a data para o formato 'YYYY-MM-DD HH:MM:SS'
            "is_author_comment": comment.is_submitter,
            "link_id": comment.link_id,  # id do post ao qual o comentário pertence
            "parent_id": comment.parent_id,  # id do comentário pai
            "permalink": comment.permalink, # link para o comentário
            "score": comment.score, # média dos votos positivos e negativos
            "fixed": comment.stickied, # se o comentário foi fixado
            "post_id": post_id # id do post ao qual o comentário pertence
        }
        # indexa o documento no Elasticsearch
        resp = self.es_client.index(index=self.target_index, id=document["id"], document=document)
        return resp