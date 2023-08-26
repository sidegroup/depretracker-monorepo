import datetime

class RedditCommentRepository:
    def __init__(self, es_client):
        self.es_client = es_client

    def store(self, target_index, comment, post_id):
        print("Storing comment: " + comment.id)
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

        resp = self.es_client.index(index=target_index, id=document["id"], document=document)
        print(resp)
        return resp