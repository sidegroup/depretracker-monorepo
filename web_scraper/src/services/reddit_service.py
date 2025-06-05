import datetime
import prawcore.exceptions
from time import sleep
from praw.models import MoreComments
import praw
from praw import Reddit


class RedditService:
    SLEEP_TIME = 5


    def __init__(self, post_repository, comment_repository,
                 client_id: str, client_secret: str, username: str, password:str, user_agent:str):
        self.post_repository = post_repository
        self.comment_repository = comment_repository

        self.redit_client = Reddit(
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            user_agent=user_agent,
        )
        _ = self.redit_client.user.me()

    # método que coleta os dados do Reddit
    def fetch_reddit_data(self, subreddits, search_strings, sort_types):

        # para cada subreddit
        for subreddit in subreddits:
        
            print(f"Subreddit: {subreddit}")
            # para cada tipo de sorte
            for sort_type in sort_types:
                print(f"Sort Type: {sort_type}")
                while True:
                    try:
                        # pesquisa as submissões no subreddit com a string de pesquisa e o tipo de sorte
                        submissions = self.redit_client \
                            .subreddit(subreddit) \
                            .search(query=search_strings, limit=None, sort=sort_type)

                        # para cada submissão
                        for submission in submissions:
                            # se a submissão foi criada após 2017, não está excluída e não está bloqueada
                            if (
                                    datetime.datetime.fromtimestamp(submission.created_utc).year > 2024
                                    and not submission.distinguished
                                    and not submission.locked
                            ):
                                #author_submission_id = submission.author.fullname if submission.author else None
                                # armazena a submissão
                                self.post_repository.store(submission)

                                # para cada comentário na submissão
                                for comment in submission.comments:
                                    # Verifica se possui comentários aninhados
                                    if isinstance(comment, MoreComments):
                                        continue

                                    #author_comment_id = comment.author.fullname if comment.author else None
                                    # armazena o comentário
                                    self.comment_repository.store(comment, submission.id)

                    # se ocorrer um erro devido a muitas solicitações
                    # aguarda um tempo e tenta novamente
                    except prawcore.exceptions.TooManyRequests as e:
                        print(f"Too many requests. Sleeping for {self.SLEEP_TIME} seconds.")
                        sleep(self.SLEEP_TIME)
                        continue

                    break

