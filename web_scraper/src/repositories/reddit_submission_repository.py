import datetime
from praw.models import Submission


class RedditSubmissionRepository:

    def __init__(self, es_client, target_index):
        self.es_client = es_client
        self.target_index = target_index

    def store(self, submission: Submission):
        print(".", end="", flush=True)
        document = {
            "author_name": submission.author.name if submission.author else "",
            "author_flair": submission.author_flair_text,
            "date": datetime.datetime.fromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
            "post_id": submission.id,
            "is_original_content": submission.is_original_content,
            "is_text": submission.is_self,
            "link_flair": submission.link_flair_text,
            "is_locked": submission.locked,
            "post_name": submission.name,
            "number_of_comments": submission.num_comments,
            "mature_content": submission.over_18,
            "permalink": submission.permalink,
            "score": submission.score,
            "text": submission.selftext,
            "spoiler": submission.spoiler,
            "fixed": submission.stickied,
            "title": submission.title,
            "upvote_ration": submission.upvote_ratio,
            "url": submission.url
        }
        resp = self.es_client.index(index=self.target_index, id=document["post_id"], document=document)
        return resp