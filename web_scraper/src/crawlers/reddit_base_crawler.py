from ..repositories.reddit_submission_repository import RedditSubmissionRepository
from ..repositories.reddit_comment_repository import RedditCommentRepository
from ..services.reddit_service import RedditService
from ..factories.elastic_search_client import ElasticsearchClientFactory

class RedditBaseCrawler:

    search_strings = ""
    # tipos de sorteamentos que podem ser usados nos subrredits
    sort_types = ["relevance", "hot", "top", "new"]
    subreddits = []
    assunto_crowler = ""

    def __init__(self, client_id: str, client_secret: str, username: str, password:str, user_agent:str, search_string: str, subreddit: list[str], assunto_crowler: str):
        self.search_strings = search_string
        self.subreddits = subreddit
        self.assunto_crowler = assunto_crowler
        self.es_client = ElasticsearchClientFactory.create()
        post_repository = RedditSubmissionRepository(self.es_client, self.assunto_crowler + "posts")
        comment_repository = RedditCommentRepository(self.es_client, self.assunto_crowler + "comments")
        self.reddit_service = RedditService(post_repository, comment_repository,
                                            client_id, client_secret, username, password, user_agent)


    
    def crawl(self,):
        self.reddit_service.fetch_reddit_data(self.subreddits,
                                              self.search_strings,
                                              self.sort_types)

    def get_search_string(self) -> str:
        return self.search_strings

    def set_search_string(self, search_string: str) -> None:
        self.search_strings = search_string

    def get_subreddit(self) -> list[str]:
        return self.subreddits
    def set_subreddit(self, subreddits: list[str]) -> None:
        self.subreddits = subreddits

    def get_assunto_crowler(self) -> str:
        return self.assunto_crowler

    def set_assunto_crowler(self, assunto_crowler: str) -> None:
        self.assunto_crowler = assunto_crowler