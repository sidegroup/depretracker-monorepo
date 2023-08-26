import datetime
import prawcore.exceptions
from time import sleep
from praw.models import MoreComments
from praw import Reddit


class RedditService:
    SLEEP_TIME = 5

    def __init__(self, post_repository, comment_repository):
        self.post_repository = post_repository
        self.comment_repository = comment_repository
        self.redit_client = Reddit(
            client_id='DzLrEIjbuDKTEirqtk3uHw',
            client_secret='5PK8_DzWN4RtuUlTVTxpONZWCtFXSw',
            username='taw-balbino',
            password='!!3uSKPvumU9Kst',
            user_agent='webcrowler /u/taw-balbino'
        )


    def fetch_reddit_data(self, subreddits, search_strings, sort_types):
        for subreddit in subreddits:
            print(f"Subreddit: {subreddit}")

            for string_de_busca in search_strings:
                print(f"Search String: {search_strings.index(string_de_busca)}")
                for sort_type in sort_types:
                    print(f"Sort Type: {sort_type}")

                    while True:
                        try:
                            submissions = self.redit_client \
                                .subreddit(subreddit) \
                                .search(query=string_de_busca, limit=None, sort=sort_type)

                            for submission in submissions:
                                if (
                                        datetime.datetime.fromtimestamp(submission.created_utc).year > 2017
                                        and not submission.distinguished
                                        and not submission.locked
                                ):
                                    self.post_repository.store(submission)

                                    for comment in submission.comments:
                                        if isinstance(comment, MoreComments):
                                            continue
                                        self.comment_repository.store(comment, submission.id)

                        except prawcore.exceptions.TooManyRequests as e:
                            print(f"Too many requests. Sleeping for {self.SLEEP_TIME} seconds.")
                            sleep(self.SLEEP_TIME)
                            continue
                        break