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
            "author_name": submission.author.name if submission.author else "", # se o autor for nulo, retorna uma string vazia
            "author_flair": submission.author_flair_text, # flair do autor
            "date": datetime.datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'), # converte a data para o formato 'YYYY-MM-DD HH:MM:SS'
            "post_id": submission.id, # id da submissão
            "is_original_content": submission.is_original_content, # se a submissão é conteúdo original
            "is_text": submission.is_self, # se a submissão é um texto
            "link_flair": submission.link_flair_text, # flair do link
            "is_locked": submission.locked, # se a submissão está bloqueada
            "post_name": submission.name, # nome da submissão
            "number_of_comments": submission.num_comments, # número de comentários
            "mature_content": submission.over_18, # se a submissão é conteúdo adulto
            "permalink": submission.permalink, # link para a submissão
            "score": submission.score, # média dos votos positivos e negativos
            "text": submission.selftext, # texto da submissão
            "spoiler": submission.spoiler, # se a submissão é um spoiler
            "fixed": submission.stickied, # se a submissão é fixada
            "title": submission.title, # título da submissão
            "upvote_ration": submission.upvote_ratio, # razão de votos positivos e negativos
            "url": submission.url # url da submissão
        }
        resp = self.es_client.index(index=self.target_index, id=document["post_id"], document=document)
        return resp