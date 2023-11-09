# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv
import json


class WebscraperPipeline:
    def process_item(self, item, spider):
        return item

class CarsPipeline(object):

    def open_spider(self, spider):
        # Load car models and trims from references.json
        with open('references.json', 'r') as file:
            self.car_models_and_trims = json.load(file)
        # Open the CSV file for writing
        self.file = open('cars.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)
        # Write the header row, now including 'model' and 'trim'
        self.writer.writerow(['title', 'price', 'mileage', 'dealer_name', 'year', 'model', 'trim'])

    def close_spider(self, spider):
        # Close the CSV file
        self.file.close()

    def process_item(self, item, spider):
        # Extract year from title and remove it from the title
        if item['title'] and len(item['title']) >= 4:
            item['year'] = item['title'][:4].strip()
            item['title'] = item['title'][4:].strip()  # Assuming the year is the first 4 characters
        else:
            item['year'] = None  # or set a default year if appropriate

        # Convert price to a float, remove any non-numeric characters
        item['price'] = float(''.join(filter(str.isdigit, item['price'])))

        # Convert mileage to an integer, remove any non-numeric characters
        item['mileage'] = int(''.join(filter(str.isdigit, item['mileage'])))

        # Check if dealer name is null or empty and set to "private" if it is
        item['dealer_name'] = item['dealer_name'].strip() if item['dealer_name'] else "private"

        # Initialize model and trim
        item['model'] = None
        item['trim'] = None

        # Attempt to extract model and trim from the title
        title = item['title'].lower()
        for car in self.car_models_and_trims:
            model = car['model'].lower()
            if model in title:
                item['model'] = car['model']
                for trim in car['trims']:
                    trim_lower = trim.lower()
                    if trim_lower in title:
                        item['trim'] = trim
                        break
                break

        # Check if any field is missing (except dealer_name which we set to "private" if missing)
        if not all(key in item for key in ('title', 'price', 'mileage', 'year', 'model', 'trim')):
            raise DropItem("Missing fields in item")

        # Write item to CSV, now including 'model' and 'trim'
        self.writer.writerow([
            item.get('title', ''),
            item.get('price', ''),
            item.get('mileage', ''),
            item.get('dealer_name', ''),
            item.get('year', ''),
            item.get('model', ''),
            item.get('trim', '')
        ])

        return item
