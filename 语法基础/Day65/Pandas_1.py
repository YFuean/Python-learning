import pandas as pb
# Pandas 读取 URL 路径的文件，得到（149 rows * 5 columns）的数据集
result = pb.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
print(result)
# 创建并保存数据
d = {'id': [1, 2], 'name': ['gz', 'lh'], 'age': [10, 12]}
df = pb.DataFrame(d)
# test.csv 文件分割符为 \t , 如果使用sep默认的逗号分隔符，读入后的数据混为一体
df.to_csv('test.csv', sep='\t')
# 读取数据，查看结果
df = pb.read_csv('test.csv')
print(df)
# sep必须设置为'\t',数据分割才会正常
df = pb.read_csv('test.csv', sep='\t')
print(df)

# 读取之列选择属性
# 参数用于选取数据文件的哪些列到 DataFrame中
# 只想使用源数据文件的id和age两列，那么可以为usecols参数赋值为['id','name']
df = pb.read_csv('test.csv', delim_whitespace=True, usecols=['id', 'name'])
print(df)
