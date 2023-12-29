from ..repositories.reddit_submission_repository import RedditSubmissionRepository
from ..repositories.reddit_comment_repository import RedditCommentRepository
from ..services.reddit_service import RedditService
from ..factories.elastic_search_client import ElasticsearchClientFactory

class RedditBaseCrawler:

    def __init__(self, client_id: str, client_secret: str, username: str, password:str, user_agent:str):
        self.es_client = ElasticsearchClientFactory.create()
        post_repository = RedditSubmissionRepository(self.es_client, self.SUBMISSION_INDEX_NAME)
        comment_repository = RedditCommentRepository(self.es_client, self.COMMENT_INDEX_NAME)
        self.reddit_service = RedditService(post_repository, comment_repository,
                                            client_id, client_secret, username, password, user_agent)
        
    
        