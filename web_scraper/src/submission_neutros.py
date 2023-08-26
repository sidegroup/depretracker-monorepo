import prawcore.exceptions
from repositories.reddit_post_repository import RedditPostRepository
from repositories.reddit_comment_repository import RedditCommentRepository
from elasticsearch import Elasticsearch
import praw
import datetime
from time import sleep


es_client = Elasticsearch(hosts=[{'host': 'es', 'port': 9200, 'use_ssl': False}])
post_repository = RedditPostRepository(es_client)
comment_repository = RedditCommentRepository(es_client)


# Autenticação na API do Reddit
reddit = praw.Reddit(client_id='DzLrEIjbuDKTEirqtk3uHw',
                     client_secret='5PK8_DzWN4RtuUlTVTxpONZWCtFXSw',
                     username='taw-balbino',
                     password='!!3uSKPvumU9Kst',
                     user_agent='webcrowler /u/taw-balbino')


search_term_1 = 'deprê NOT ansiedade NOT chorar NOT morrer NOT matar NOT medo NOT crises NOT chorando NOT Só NOT sozinho NOT solidão NOT dedolado NOT desolado NOT morto NOT vazio NOT suícidio NOT surto NOT surtei NOT surtar NOT depressivo NOT depressão NOT ansioso NOT ansiosa NOT desespero NOT desesperado NOT desesperada NOT solitário NOT melancólico NOT desânimo NOT tristeza NOT depresso NOT infeliz NOT angustiado NOT choro NOT cortar NOT corte NOT culpa NOT culpado NOT culpando NOT deprimido NOT desamparado'
search_term_2 = 'desanimado NOT desmotivado NOT doloroso NOT dor NOT dores NOT frustrado NOT insonia NOT machucado NOT morreu NOT morte NOT noite NOT pranto NOT pulsos NOT punicao NOT sangrar NOT sangrento NOT solidao NOT solitario NOT sozinho NOT suicidar NOT suicidas NOT suicidio NOT tedio NOT triste NOT desesperança'

search_strings = [search_term_1, search_term_2]
sort_types = ["relevance", "hot", "top", "new"]
subreddits = ["ConselhosLegais", "30mais", "PergunteReddit", "BrasildoB",
              "conversasserias", "filmeseseries", "Pesca", "viagens", "futebol", "vasco", "carros"]


for subreddit in subreddits:
    for string_busca in search_strings:
        for sort_type in sort_types:
            while True:
                try:
                    submissions = reddit.subreddit(subreddit).search(
                        string_busca, limit=None, sort=sort_type)
                    for submission in submissions:
                        if (
                                datetime.datetime.fromtimestamp(submission.created_utc).year > 2017
                                and not (submission.distinguished)
                                and not (submission.locked)
                        ):
                            post_repository.store("post_neutro", submission)

                            for comment in submission.comments:
                                comment_repository.store("comment_neutro", comment, submission.id)

                except prawcore.exceptions.TooManyRequests as e:
                    print(f"Too many requests. Sleeping for {e.retry_after} seconds.")
                    sleep(e.retry_after)
                    continue
                break
