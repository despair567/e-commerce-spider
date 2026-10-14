BOT_NAME = 'spider_module'
SPIDER_MODULES = ['spider_module.spiders']
NEWSPIDER_MODULE = 'spider_module.spiders'

# 遵守 robots.txt 规则（若要强行爬取可设为 False，但课程设计建议 True）
ROBOTSTXT_OBEY = True

# 反爬延迟控制
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 10

# 开启中间件和管道
DOWNLOADER_MIDDLEWARES = {
   'spider_module.middlewares.CustomAntiSpiderMiddleware': 543,
}
ITEM_PIPELINES = {
   'spider_module.pipelines.EcommercePipeline': 300,
}