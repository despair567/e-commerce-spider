import scrapy
from spider_module.items import EcommerceItem
import random

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['books.toscrape.com']

    def __init__(self, keyword='手机', *args, **kwargs):
        super(EcommerceSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword
        # 模拟电商排行榜页面
        self.start_urls = ['https://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        products = response.css('article.product_pod')
        for product in products:
            item = EcommerceItem()
            item['name'] = product.css('h3 a::attr(title)').get()
            item['price'] = product.css('p.price_color::text').get()
            item['rating'] = product.css('p.star-rating::attr(class)').get().split()[1]  # 提取评分等级
            item['url'] = response.urljoin(product.css('h3 a::attr(href)').get())
            item['category'] = self.keyword

            # 模拟真实电商才有的字段
            item['sales'] = random.randint(100, 10000)
            item['shop_name'] = "演示店铺"
            item['comments'] = random.randint(10, 500)
            item['listing_time'] = "2023-01-01"

            yield item

        # 翻页逻辑
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)