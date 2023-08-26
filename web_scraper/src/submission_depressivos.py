from builtins import print

from repositories.reddit_post_repository import RedditPostRepository
from repositories.reddit_comment_repository import RedditCommentRepository
from elasticsearch import Elasticsearch
import praw
import datetime
import time

es_client = Elasticsearch(hosts=[{'host': 'es', 'port': 9200, 'use_ssl': False}])
post_repository = RedditPostRepository(es_client)
comment_repository = RedditCommentRepository(es_client)

reddit = praw.Reddit(
    client_id='DzLrEIjbuDKTEirqtk3uHw',
    client_secret='5PK8_DzWN4RtuUlTVTxpONZWCtFXSw',
    username='taw-balbino',
    password='!!3uSKPvumU9Kst',
    user_agent='webcrowler /u/taw-balbino'
)

string_de_busca_1 = 'deprê OR ansiedade OR chorar OR morrer OR matar OR medo OR crises OR chorando OR Só OR sozinho OR solidão OR dedolado OR desolado OR morto OR vazio OR suícidio OR surto OR surtei OR surtar OR depressivo OR depressão OR ansioso OR ansiosa OR desespero OR desesperado OR desesperada OR solitário OR melancólico OR desânimo OR tristeza OR depresso OR infeliz OR angustiado OR choro OR cortar OR corte OR culpa OR culpado OR culpando OR deprimido OR desamparado'
string_de_busca_2 = 'desanimado OR desmotivado OR doloroso OR dor OR dores OR frustrado OR insonia OR machucado OR morreu OR morte OR noite OR pranto OR pulsos OR punicao OR sangrar OR sangrento OR solidao OR solitario OR sozinho OR suicidar OR suicidas OR suicidio OR tedio OR triste OR desesperança'


search_strings = [string_de_busca_1, string_de_busca_2]
sort_types = ["relevance", "hot", "top", "new"]
subreddits = ["arco_iris", "desabafos", "desabafo",
              "relacionamentos", "transbr", "EuSouOBabaca", "BissexualidadeBr"]


for subreddit in subreddits:
    for string_de_busca in search_strings:
        for sort_type in sort_types:
            while True:
                try:
                    print("Subreddit: " + subreddit)
                    submissions = reddit\
                        .subreddit(subreddit)\
                        .search(query=string_de_busca, limit=None, sort=sort_type)

                    for submission in submissions:
                        if (
                            datetime.datetime.fromtimestamp(submission.created_utc).year > 2017
                            and not submission.distinguished
                            and not submission.locked
                        ):
                            print("Post: " + submission.title)
                            post_repository.store("reddit_depressed_posts", submission)

                            for comment in submission.comments:
                                print("Comment: " + comment.body)
                                comment_repository.store("reddit_depressed_comments", comment, submission.id)

                except Exception as e:
                    time.sleep(5)
                    continue

                break
