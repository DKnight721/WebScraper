import scrapy

class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['cars.com']
    start_urls = [input("enter in your url")] #['https://www.cars.com/shopping/results/?dealer_id=&keyword=&list_price_max=&list_price_min=&makes[]=lexus&maximum_distance=all&mileage_max=&models[]=lexus-is_200t&models[]=lexus-is_250&models[]=lexus-is_250c&models[]=lexus-is_300&models[]=lexus-is_350&models[]=lexus-is_350c&models[]=lexus-is_500&models[]=lexus-is_f&monthly_payment=&page_size=20&sort=best_match_desc&stock_type=all&year_max=&year_min=&zip=80259']

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
        # Select the 'Next' link directly using its unique ID or class
        next_page_link = response.css('a.sds-pagination__control[id="next_paginate"]::attr(href)').get()
        # Join the relative URL with the response URL to get the absolute URL
        next_page_url = response.urljoin(next_page_link) if next_page_link else None

        # Check if the "next" page link is not the current page
        if next_page_url and next_page_url != response.url:
            yield response.follow(next_page_url, callback=self.parse)

