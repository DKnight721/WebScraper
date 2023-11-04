import scrapy


class KslSpider(scrapy.Spider):
    name = "ksl"
    allowed_domains = ["classifieds.ksl.com"]
    start_urls = ["https://classifieds.ksl.com"]

    def parse(self, response):
        pass
