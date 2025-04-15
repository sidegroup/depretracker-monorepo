from ..repositories.reddit_submission_repository import RedditSubmissionRepository
from ..repositories.reddit_comment_repository import RedditCommentRepository
from ..services.reddit_service import RedditService

class RedditBaseCrawler:

    search_strings = ""
    # Tipos de ordenação que podem ser usados nos subreddits
    sort_types = ["relevance", "hot", "top", "new"]
    subreddits = []
    assunto_crowler = ""

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        username: str,
        password: str,
        user_agent: str,
        search_string: str,
        subreddit: list[str],
        post_repository: RedditSubmissionRepository,
        comment_repository: RedditCommentRepository
    ):
        self.search_strings = search_string
        self.subreddits = subreddit
        self.assunto_crowler = ""
        self.reddit_service = RedditService(
            post_repository,
            comment_repository,
            client_id,
            client_secret,
            username,
            password,
            user_agent
        )

    def crawl(self):
        self.reddit_service.fetch_reddit_data(
            self.subreddits,
            self.search_strings,
            self.sort_types
        )

    def get_search_string(self) -> str:
        return self.search_strings

    def set_search_string(self, search_string: str) -> None:
        self.search_strings = search_string

    def get_subreddit(self) -> list[str]:
        return self.subreddits

    def set_subreddit(self, subreddits: list[str]) -> None:
        self.subreddits = subreddits
