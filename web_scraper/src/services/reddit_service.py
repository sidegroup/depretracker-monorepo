import datetime
import prawcore.exceptions
from time import sleep
from praw.models import MoreComments
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
            user_agent=user_agent
        )

    def fetch_reddit_data(self, subreddits, search_strings, sort_types):
        for subreddit in subreddits:
            print(f"Subreddit: {subreddit}")
            for sort_type in sort_types:
                print(f"Sort Type: {sort_type}")
                while True:
                    try:
                        submissions = self.redit_client \
                            .subreddit(subreddit) \
                            .search(query=search_strings, limit=None, sort=sort_type)

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