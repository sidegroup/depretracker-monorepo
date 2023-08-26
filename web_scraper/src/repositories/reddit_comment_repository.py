import datetime
from praw.models import Comment


class RedditCommentRepository:
    def __init__(self, es_client, target_index):
        self.es_client = es_client
        self.target_index = target_index

    def store(self, comment: Comment, post_id: int):
        print(".", end="", flush=True)
        document = {
            "id": comment.id,
            "author_name": comment.author.name if comment.author else "",
            "body": comment.body,
            "body_html": comment.body_html,
            "date": datetime.datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
            "is_author_comment": comment.is_submitter,
            "link_id": comment.link_id,
            "parent_id": comment.parent_id,
            "permalink": comment.permalink,
            "score": comment.score,
            "fixed": comment.stickied,
            "post_id": post_id
        }

        resp = self.es_client.index(index=self.target_index, id=document["id"], document=document)
        return resp