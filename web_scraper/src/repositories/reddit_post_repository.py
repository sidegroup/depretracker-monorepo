import datetime

class RedditPostRepository:
    def __init__(self, es_client):
        self.es_client = es_client

    def store(self, target_index, post):
        print("Storing post: " + post.id)
        document = {
            "author_name": post.author.name if post.author else "",
            "author_flair": post.author_flair_text,
            "date": datetime.datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
            "post_id": post.id,
            "is_original_content": post.is_original_content,
            "is_text": post.is_self,
            "link_flair": post.link_flair_text,
            "is_locked": post.locked,
            "post_name": post.name,
            "number_of_comments": post.num_comments,
            "mature_content": post.over_18,
            "permalink": post.permalink,
            "score": post.score,
            "text": post.selftext,
            "spoiler": post.spoiler,
            "fixed": post.stickied,
            "title": post.title,
            "upvote_ration": post.upvote_ratio,
            "url": post.url
        }

        resp = self.es_client.index(index=target_index, id=document["id"], document=document)
        print(resp)
        return resp