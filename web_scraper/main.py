import sys
from web_scraper.src.crawlers.depressed_submissions_crawler import DepressedSubmissionsCrawler
from web_scraper.src.crawlers.neutral_submissions_crawler import NeutralSubmissionsCrawler


def main() -> int:
    DepressedSubmissionsCrawler().crawl()
    NeutralSubmissionsCrawler().crawl()
    return 0


if __name__ == "__main__":
    sys.exit(main())