'''
使用Pandas做数据分析
'''
import pandas as pb

path1 = './res/csv/data.csv'
# 数据集存入一个名为chipo的数据框
chipo = pb.read_csv(path1, sep='\t')
# 查看前10行
print(chipo.head(10))
# 数据集中有多少列
print(chipo.shape[1])
# 打印出全部列名
print(chipo.columns)
# 数据集的索引
print(chipo.index)
#
# print(chipo['name'].nunique())
