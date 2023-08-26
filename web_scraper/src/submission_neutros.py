import praw
import datetime
import time
from elasticsearch import Elasticsearch


es_client = Elasticsearch(
    hosts=[{'host': 'es', 'port': 9200, 'use_ssl': False}])

# Autenticação na API do Reddit
reddit = praw.Reddit(client_id='DzLrEIjbuDKTEirqtk3uHw',
                     client_secret='5PK8_DzWN4RtuUlTVTxpONZWCtFXSw',
                     username='taw-balbino',
                     password='!!3uSKPvumU9Kst',
                     user_agent='webcrowler /u/taw-balbino')


string_de_busca_1 = 'deprê NOT ansiedade NOT chorar NOT morrer NOT matar NOT medo NOT crises NOT chorando NOT Só NOT sozinho NOT solidão NOT dedolado NOT desolado NOT morto NOT vazio NOT suícidio NOT surto NOT surtei NOT surtar NOT depressivo NOT depressão NOT ansioso NOT ansiosa NOT desespero NOT desesperado NOT desesperada NOT solitário NOT melancólico NOT desânimo NOT tristeza NOT depresso NOT infeliz NOT angustiado NOT choro NOT cortar NOT corte NOT culpa NOT culpado NOT culpando NOT deprimido NOT desamparado'
string_de_busca_2 = 'desanimado NOT desmotivado NOT doloroso NOT dor NOT dores NOT frustrado NOT insonia NOT machucado NOT morreu NOT morte NOT noite NOT pranto NOT pulsos NOT punicao NOT sangrar NOT sangrento NOT solidao NOT solitario NOT sozinho NOT suicidar NOT suicidas NOT suicidio NOT tedio NOT triste NOT desesperança'

strings_de_busca = [string_de_busca_1, string_de_busca_2]

sort_types = ["relevance", "hot", "top", "new"]
subreddits = ["ConselhosLegais", "30mais", "PergunteReddit", "BrasildoB",
              "conversasserias", "filmeseseries", "Pesca", "viagens", "futebol", "vasco", "carros"]


for subreddit in subreddits:
    for string_busca in strings_de_busca:
        for sort_type in sort_types:
            while True:
                try:
                    submissions = reddit.subreddit(subreddit).search(
                        string_busca, limit=None, sort=sort_type)
                    for submission in submissions:
                        if datetime.datetime.fromtimestamp(submission.created_utc).year > 2017 and not (submission.distinguished) and not (submission.locked):
                            post = {
                                "autor": submission.author.name,
                                "rotuloDoAutor": submission.author_flair_text,
                                "data": datetime.datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                                # campo referente se a submissão foi destacado pelo admin,moderator ou é um normal
                                "destaque": submission.distinguished,
                                "editado": submission.edited,
                                "id": submission.id,
                                "EhOriginal": submission.is_original_content,
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
                            resp = es_client.index(index="post_neutro",
                                                id=post["id"], document=post)

                            for comment in submission.comments:
                                comentario = {
                                    "autor": comment.author.name if comment.author else "",
                                    "bodyEmMarkdown": comment.body,
                                    "bodyEmHtml": comment.body_html,
                                    "data": datetime.datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                                    "destaque": comment.distinguished,
                                    "editado": comment.edited,
                                    "id": comment.id,
                                    "oAutorDoPostEhDoComentario": comment.is_submitter,
                                    "hierarquia": comment.link_id,
                                    "paiDoComentario": comment.parent_id,
                                    "linkFixo": comment.permalink,
                                    "popularidade": comment.score,
                                    "fixado": comment.stickied,
                                    "id_submission": submission.id
                                }
                                print(comentario["bodyEmMarkdown"])

                                resp = es_client.index(
                                    index="comentario_neutro", id=comentario["id"], document=comentario)                   
                except:
                    time.sleep(5)
                
                break
