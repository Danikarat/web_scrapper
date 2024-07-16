from scrapy import Spider


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["https://stackoverfow.com/questions?pagesize=50&sort=newest",]