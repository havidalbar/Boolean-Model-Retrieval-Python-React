from retrieval.sehatq_spider import SehatQSpider
from scrapy.crawler import CrawlerProcess


process = CrawlerProcess()
process.crawl(SehatQSpider, write_path='retrieval/resources/data_scrape.txt')
process.start()
