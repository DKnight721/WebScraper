import scrapy

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip']

    def parse(self, response):
        ip_address = response.json()['origin']
        self.logger.info(f'My current IP address is: {ip_address}')
