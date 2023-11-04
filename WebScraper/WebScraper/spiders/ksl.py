import scrapy


class eBaySpider(scrapy.Spider):
    name = "ebay"
    allowed_domains = ["ebay.com"]
    start_urls = ["https://www.ebay.com/sch/i.html?_from=R40&_nkw=macbook+pro+m1+pro&_sacat=0&Screen%2520Size=14%252D14%252E9%2520in%7C16%252D16%252E9%2520in&_oaa=1&rt=nc&Processor=Apple%2520M1%2520Max%7CApple%2520M1%2520Pro%7CApple%2520M2%2520Pro&_dcat=111422&_ipg=240"]

    def parse(self, response):
        pass
