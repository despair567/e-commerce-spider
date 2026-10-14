import scrapy

class EcommerceItem(scrapy.Item):
    name = scrapy.Field()          # 商品名称
    price = scrapy.Field()         # 价格
    sales = scrapy.Field()         # 销量
    shop_name = scrapy.Field()     # 店铺名
    url = scrapy.Field()           # 商品链接
    comments = scrapy.Field()      # 评论数
    rating = scrapy.Field()        # 评分
    listing_time = scrapy.Field()  # 上架时间
    category = scrapy.Field()      # 类别（由关键词或排行榜页面决定）