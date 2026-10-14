import pandas as pd


class DataAnalyzer:
    def __init__(self, raw_data_path, output_path):
        self.raw_data_path = raw_data_path
        self.output_path = output_path

    def clean_data(self):
        print("正在加载原始数据...")
        df = pd.read_csv(self.raw_data_path)

        # 1. 去重（根据商品名称和店铺去重）
        df.drop_duplicates(subset=['name', 'shop_name'], keep='first', inplace=True)

        # 2. 缺失值处理
        df.fillna({'comments': 0, 'sales': 0}, inplace=True)

        # 3. 格式标准化
        # 价格格式处理 (例如去掉 £ 符号转为数字)
        df['price'] = df['price'].astype(str).str.replace('£', '').astype(float)

        # 将评分文字转为数字
        rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        df['rating_num'] = df['rating'].map(rating_map).fillna(0)

        # 4. 过滤异常数据
        df = df[df['price'] > 0]

        df.to_csv(self.output_path, index=False, encoding='utf-8-sig')
        print(f"数据清洗完成，保存至 {self.output_path}")
        return df

    def generate_hot_rank(self, df):
        # 按销量降序排序，生成热销榜单 TOP 50
        hot_rank = df.sort_values(by='sales', ascending=False).head(50)
        hot_rank.to_excel('data/Top50_热销榜单.xlsx', index=False)
        print("热销榜单 TOP 50 已生成！")
        return hot_rank

    def multi_dimension_analysis(self, df):
        # 维度1：价格区间统计
        bins = [0, 10, 20, 30, 50, 100, float('inf')]
        labels = ['10元以下', '10-20元', '20-30元', '30-50元', '50-100元', '100元以上']
        df['price_range'] = pd.cut(df['price'], bins=bins, labels=labels)
        price_dist = df['price_range'].value_counts()

        # 维度2：店铺热销 TOP10
        shop_top10 = df.groupby('shop_name')['sales'].sum().sort_values(ascending=False).head(10)

        return price_dist, shop_top10