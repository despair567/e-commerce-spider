#将爬虫数据写入csv
import csv

class EcommercePipeline:
    def open_spider(self, spider):
        self.file = open('data/raw_products.csv', 'w', newline='', encoding='utf-8-sig')
        self.writer = csv.DictWriter(self.file, fieldnames=[
            'name', 'price', 'sales', 'shop_name', 'url',
            'comments', 'rating', 'listing_time', 'category'
        ])
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.file.close()