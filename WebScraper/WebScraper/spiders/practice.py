import scrapy

class PagesSpider(scrapy.Spider):
    name = 'practice'
    allowed_domains = ['scrapethissite.com']
    start_urls = ['https://www.scrapethissite.com/pages/']

    def parse(self, response):
        # Extract the content using css selectors
        page_links = response.css('div.page a::attr(href)').extract()
        for link in page_links:
            # Provide the absolute URL by joining the relative URL with the base one
            absolute_url = response.urljoin(link)
            yield scrapy.Request(absolute_url, callback=self.parse_page)

    def parse_page(self, response):
        # Define the data structure to extract
        data = {
            'title': response.css('h1::text').get(),
            'content': response.css('div.page-content::text').getall(),
        }
        yield data
