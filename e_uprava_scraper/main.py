from e_uprava_scraper.spiders.a_category_scraper import ACategoryScraperSpider
from scrapy.crawler import CrawlerProcess



def main():
    process = CrawlerProcess()
    process.crawl(ACategoryScraperSpider)
    process.start()

if __name__ == '__main__':
    main()
