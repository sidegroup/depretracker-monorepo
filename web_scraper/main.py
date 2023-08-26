import sys
from time import sleep
from src.crawlers.depressed_submissions_crawler import DepressedSubmissionsCrawler
from src.crawlers.neutral_submissions_crawler import NeutralSubmissionsCrawler
from src.services.elasticsearch_service import ElasticSearchService
from src.factories.elastic_search_client import ElasticsearchClientFactory


def main() -> int:
    while not ElasticSearchService(
        ElasticsearchClientFactory.create()
    ).readiness_check():
        print("Waiting for Elasticsearch to be ready")
        sleep(5)


    DepressedSubmissionsCrawler().crawl()
    NeutralSubmissionsCrawler().crawl()
    return 0


if __name__ == "__main__":
    sys.exit(main())