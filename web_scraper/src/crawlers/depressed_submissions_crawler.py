from .reddit_base_crawler import RedditBaseCrawler


class DepressedSubmissionsCrawler(RedditBaseCrawler):
    search_strings = ""
    sort_types = ["relevance", "hot", "top", "new"]
    subreddits = []
    SUBMISSION_INDEX_NAME = "reddit_depressed_posts"
    COMMENT_INDEX_NAME = "reddit_depressed_comments"

    def __init__(self, client_id: str, client_secret: str, username: str, password:str, user_agent:str):
        super().__init__(client_id, client_secret, username, password, user_agent)

    def crawl(self,):
        self.reddit_service.fetch_reddit_data(self.subreddits,
                                              self.search_strings,
                                              self.sort_types)
        
        
    def set_subreddit(self, subreddits: list[str]) -> None:
        self.subreddits = subreddits
        
    def set_search_string(self, search_string: str) -> None:
        self.search_strings = search_string
        
    def get_submission_index_name(self) -> str:
        return self.SUBMISSION_INDEX_NAME
    
    def get_comment_index_name(self) -> str:
        return self.COMMENT_INDEX_NAME
    
    
    