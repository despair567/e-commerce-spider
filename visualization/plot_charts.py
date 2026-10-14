import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

class Visualizer:
    def __init__(self, df):
        self.df = df

    def plot_hot_rank_bar(self, top_n=10):
        top_products = self.df.sort_values(by='sales', ascending=False).head(top_n)
        plt.figure(figsize=(12, 6))
        sns.barplot(x='sales', y='name', data=top_products, palette='viridis')
        plt.title(f'热销商品 TOP {top_n}')
        plt.xlabel('销量')
        plt.ylabel('商品名称')
        plt.tight_layout()
        plt.savefig('data/Top10_热销商品柱状图.png', dpi=300)
        plt.show()

    def plot_price_distribution_pie(self, price_dist):
        plt.figure(figsize=(8, 8))
        plt.pie(price_dist, labels=price_dist.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
        plt.title('商品价格区间分布')
        plt.savefig('data/价格区间分布饼图.png', dpi=300)
        plt.show()

    def plot_shop_top10(self, shop_top10):
        plt.figure(figsize=(10, 5))
        shop_top10.plot(kind='bar', color='coral')
        plt.title('店铺热销 TOP10')
        plt.xlabel('店铺名称')
        plt.ylabel('总销量')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('data/店铺热销TOP10.png', dpi=300)
        plt.show()