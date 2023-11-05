import scrapy

class eBaySpider(scrapy.Spider):
    name = "ebay"
    allowed_domains = ["ebay.com"]
    start_urls = [
        "https://www.ebay.com/sch/i.html?_from=R40&_nkw=macbook+pro+m1+pro&_sacat=0&LH_TitleDesc=0&_fsrp=1&_ipg=200&Screen%2520Size=14%252D14%252E9%2520in%7C16%252D16%252E9%2520in&_oaa=1&rt=nc&Processor=Apple%2520M1%2520Pro%7CApple%2520M1%2520Max&_dcat=111422"
    ]

    def parse(self, response):
        # Loop over each listing
        listings = response.css('li.s-item')
        for listing in listings:
            yield {
                'title': listing.css('div.s-item__title > span::text').get(default='').strip(),
                'price': listing.css('span.s-item__price::text').get(default='').strip(),
                'subtitle': listing.css('div.s-item__subtitle > span::text').get(default='').strip(),
                'shipping': listing.css('span.s-item__shipping.s-item__logisticsCost::text').get(default='').strip(),
                # If there are additional details you want to scrape, add them here.
            }

        # Follow pagination link
        next_page = response.css('a.pagination__next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
