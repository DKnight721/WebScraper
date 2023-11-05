import scrapy

class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['cars.com']
    start_urls = ['https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=porsche&maximum_distance=all&mileage_max=&models[]=porsche-cayenne&monthly_payment=&page=1&page_size=100&sort=best_match_desc&stock_type=all&year_max=&year_min=&zip=80259']

    def parse(self, response):
        # Loop through each vehicle card
        for vehicle in response.css('div.vehicle-card'):
            yield {
                'title': vehicle.css('h2.title::text').get(),
                'price': vehicle.css('span.primary-price::text').get(),
                'mileage': vehicle.css('div.mileage::text').get(),
                'dealer_name': vehicle.css('div.dealer-name strong::text').get(),
                # Add more fields as needed
            }

        # Pagination logic
        # Find all available pages from the pagination section
        page_links = response.css('ul.sds-pagination__list li a::attr(href)').getall()
        # The last page link in the list should be the "next" page
        next_page = page_links[-1] if page_links else None

        # Check if the "next" page link is not the current page
        if next_page and response.urljoin(next_page) != response.url:
            yield response.follow(next_page, callback=self.parse)
