from elasticsearch import Elasticsearch
import praw
import datetime
import time


# Autenticação na API do Reddit


es_client = Elasticsearch(hosts=[{'host': 'es', 'port': 9200, 'use_ssl': False}])
reddit = praw.Reddit(client_id='DzLrEIjbuDKTEirqtk3uHw',
                     client_secret='5PK8_DzWN4RtuUlTVTxpONZWCtFXSw',
                     username='taw-balbino',
                     password='!!3uSKPvumU9Kst',
                     user_agent='webcrowler /u/taw-balbino')


string_de_busca_1 = 'deprê OR ansiedade OR chorar OR morrer OR matar OR medo OR crises OR chorando OR Só OR sozinho OR solidão OR dedolado OR desolado OR morto OR vazio OR suícidio OR surto OR surtei OR surtar OR depressivo OR depressão OR ansioso OR ansiosa OR desespero OR desesperado OR desesperada OR solitário OR melancólico OR desânimo OR tristeza OR depresso OR infeliz OR angustiado OR choro OR cortar OR corte OR culpa OR culpado OR culpando OR deprimido OR desamparado'
string_de_busca_2 = 'desanimado OR desmotivado OR doloroso OR dor OR dores OR frustrado OR insonia OR machucado OR morreu OR morte OR noite OR pranto OR pulsos OR punicao OR sangrar OR sangrento OR solidao OR solitario OR sozinho OR suicidar OR suicidas OR suicidio OR tedio OR triste OR desesperança'

strings_de_busca = [string_de_busca_1, string_de_busca_2]
sort_types = ["relevance", "hot", "top", "new"]
subreddits = ["arco_iris", "desabafos", "desabafo",
              "relacionamentos", "transbr", "EuSouOBabaca", "BissexualidadeBr"]

for subreddit in subreddits:
    for string_de_busca in strings_de_busca:
        for sort_type in sort_types:
            while True:
                try:
                    submissions = reddit.subreddit(subreddit).search(
                        query=string_de_busca, limit=None, sort=sort_type)
                    for submission in submissions:
                        if datetime.datetime.fromtimestamp(submission.created_utc).year > 2017 and not (submission.distinguished) and not (submission.locked):
                            for submission in submissions:
                                post = {
                                    "autor": submission.author.name if submission.author else "",
                                    "rotuloDoAutor": submission.author_flair_text,
                                    "data": datetime.datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                                    "id": submission.id,
                                    "ehOriginal": submission.is_original_content,
                                    "ehTexto": submission.is_self,
                                    "nomeDoRotulo": submission.link_flair_text,
                                    "bloqueado": submission.locked,
                                    "tipoMaisIdentificador": submission.name,
                                    "numeroComentarios": submission.num_comments,
                                    "maior18": submission.over_18,
                                    "link": submission.permalink,
                                    "popularidade": submission.score,
                                    "texto": submission.selftext,
                                    "spoiler": submission.spoiler,
                                    "fixado": submission.stickied,
                                    "titulo": submission.title,
                                    "mediaDeVotosPositivos": submission.upvote_ratio,
                                    "url": submission.url
                                }
                                resp = es_client.index(index="post_depressivo", id=post["id"], document=post)
                                
                                for comment in submission.comments:
                                    comentario = {
                                        "autor": comment.author.name if comment.author else "",
                                        "bodyEmMarkdown": comment.body,
                                        "bodyEmHtml": comment.body_html,
                                        "data": datetime.datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                                        "id": comment.id,
                                        "oAutorDoPostEhDoComentario": comment.is_submitter,
                                        "hierarquia": comment.link_id,
                                        "paiDoComentario": comment.parent_id,
                                        "linkFixo": comment.permalink,
                                        "popularidade": comment.score,
                                        "fixado": comment.stickied,
                                        "id_submission": submission.id
                                    }
                                    resp = es_client.index(index="comentario_depressivo", id=comentario["id"], document=comentario)
                except Exception as e:
                    time.sleep(5)

                
                break
