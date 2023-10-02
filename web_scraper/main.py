import sys
from time import sleep
from src.crawlers.depressed_submissions_crawler import DepressedSubmissionsCrawler
from src.crawlers.neutral_submissions_crawler import NeutralSubmissionsCrawler
from src.services.elasticsearch_service import ElasticSearchService
from src.factories.elastic_search_client import ElasticsearchClientFactory
from src.commands.create_csv import CreateCsv


def main() -> int:
    while not ElasticSearchService(
        ElasticsearchClientFactory.create()
    ).readiness_check():
        print("Waiting for Elasticsearch to be ready")
        sleep(5)


    DepressedSubmissionsCrawler().crawl()
    NeutralSubmissionsCrawler().crawl()
    CreateCsv().for_submissions("reddit_neutral_submissions")
    CreateCsv().for_comments("reddit_neutral_comments")
    CreateCsv().for_submissions("reddit_depressed_posts")
    CreateCsv().for_comments("reddit_depressed_comments")
    return 0


if __name__ == "__main__":
    sys.exit(main())