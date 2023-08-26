from .reddit_base_crawler import RedditBaseCrawler


class DepressedSubmissionsCrawler(RedditBaseCrawler):
    SEARCH_STRINGS = [
        'deprê OR ansiedade OR chorar OR morrer OR matar OR medo OR crises OR chorando OR Só OR sozinho OR solidão OR dedolado OR desolado OR morto OR vazio OR suícidio OR surto OR surtei OR surtar OR depressivo OR depressão OR ansioso OR ansiosa OR desespero OR desesperado OR desesperada OR solitário OR melancólico OR desânimo OR tristeza OR depresso OR infeliz OR angustiado OR choro OR cortar OR corte OR culpa OR culpado OR culpando OR deprimido OR desamparado',
        'desanimado OR desmotivado OR doloroso OR dor OR dores OR frustrado OR insonia OR machucado OR morreu OR morte OR noite OR pranto OR pulsos OR punicao OR sangrar OR sangrento OR solidao OR solitario OR sozinho OR suicidar OR suicidas OR suicidio OR tedio OR triste OR desesperança'
    ]
    SORT_TYPES = ["relevance", "hot", "top", "new"]
    SUBREDDITS = ["arco_iris", "desabafos", "desabafo", "relacionamentos", "transbr", "EuSouOBabaca", "BissexualidadeBr"]
    SUBMISSION_INDEX_NAME = "reddit_depressed_posts"
    COMMENT_INDEX_NAME = "reddit_depressed_comments"

    def __init__(self):
        super().__init__()

    def crawl(self):
        self.reddit_service.fetch_reddit_data(self.SUBREDDITS,
                                              self.SEARCH_STRINGS,
                                              self.SORT_TYPES)