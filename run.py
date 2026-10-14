import logging
import os
import pandas as pd
from spider_module.spiders.ecommerce import EcommerceSpider  # 根据你的实际爬虫文件名调整
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from data_process.analyzer import DataAnalyzer
from visualization.plot_charts import Visualizer

# 配置日志
logging.basicConfig(
    filename='logs/system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def run_system():
    logging.info("==== 电商热销榜单系统开始运行 ====")

    # 1. 必须在这里创建目录，确保 Scrapy 的 Pipeline 能写入文件！
    os.makedirs('data', exist_ok=True)
    os.makedirs('logs', exist_ok=True)

    try:
        # 2. 数据采集
        logging.info("开始执行 Scrapy 爬虫...")
        process = CrawlerProcess(get_project_settings())
        process.crawl(EcommerceSpider, keyword='手机')
        process.start()  # 阻塞直到爬虫结束
        logging.info("数据采集完成...")

        # 检查文件是否真的生成了
        if not os.path.exists('data/raw_products.csv'):
            raise FileNotFoundError(
                "Scrapy 运行结束，但未生成 data/raw_products.csv。请检查 pipelines.py 是否配置正确，或者 data 文件夹是否存在。")

        # 3. 数据清洗与处理
        analyzer = DataAnalyzer('data/raw_products.csv', 'data/clean_products.csv')
        df = analyzer.clean_data()

        # 4. 榜单生成
        hot_rank = analyzer.generate_hot_rank(df)

        # 5. 多维度分析
        price_dist, shop_top10 = analyzer.multi_dimension_analysis(df)
        logging.info(f"价格区间分布: {price_dist.to_dict()}")

        # 6. 可视化
        viz = Visualizer(df)
        viz.plot_hot_rank_bar()
        viz.plot_price_distribution_pie(price_dist)
        viz.plot_shop_top10(shop_top10)

        # 7. 导出报告
        with pd.ExcelWriter('data/final_report.xlsx') as writer:
            df.to_excel(writer, sheet_name='清洗后数据', index=False)
            hot_rank.to_excel(writer, sheet_name='热销榜TOP50', index=False)
            price_dist.to_excel(writer, sheet_name='价格区间分布')
            shop_top10.to_excel(writer, sheet_name='店铺热销TOP10')

        logging.info("报告导出成功，系统运行结束。")
        print("系统运行成功！请查看 data 目录下的报告和图表。")

    except Exception as e:
        logging.error(f"系统运行出错: {e}", exc_info=True)
        print(f"运行出错: {e}")


if __name__ == "__main__":
    run_system()

if __name__ == "__main__":
    # 确保目录存在
    os.makedirs('data', exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    run_system()