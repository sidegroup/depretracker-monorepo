from .reddit_base_crawler import RedditBaseCrawler


class NeutralSubmissionsCrawler(RedditBaseCrawler):
    SEARCH_STRINGS = [
        'deprê NOT ansiedade NOT chorar NOT morrer NOT matar NOT medo NOT crises NOT chorando NOT Só NOT sozinho NOT solidão NOT dedolado NOT desolado NOT morto NOT vazio NOT suícidio NOT surto NOT surtei NOT surtar NOT depressivo NOT depressão NOT ansioso NOT ansiosa NOT desespero NOT desesperado NOT desesperada NOT solitário NOT melancólico NOT desânimo NOT tristeza NOT depresso NOT infeliz NOT angustiado NOT choro NOT cortar NOT corte NOT culpa NOT culpado NOT culpando NOT deprimido NOT desamparado',
        'desanimado NOT desmotivado NOT doloroso NOT dor NOT dores NOT frustrado NOT insonia NOT machucado NOT morreu NOT morte NOT noite NOT pranto NOT pulsos NOT punicao NOT sangrar NOT sangrento NOT solidao NOT solitario NOT sozinho NOT suicidar NOT suicidas NOT suicidio NOT tedio NOT triste NOT desesperança'
    ]
    SORT_TYPES = ["relevance", "hot", "top", "new"]
    SUBREDDITS = ["ConselhosLegais", "30mais", "PergunteReddit", "BrasildoB", "conversasserias", "filmeseseries", "Pesca", "viagens", "futebol", "vasco", "carros"]
    SUBMISSION_INDEX_NAME = "reddit_neutral_submissions"
    COMMENT_INDEX_NAME = "reddit_neutral_comments"

    def __init__(self):
        super().__init__()

    def crawl(self):
        self.reddit_service.fetch_reddit_data(self.SUBREDDITS,
                                              self.SEARCH_STRINGS,
                                              self.SORT_TYPES)