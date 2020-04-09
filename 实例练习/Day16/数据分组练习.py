'''
数据分组练习
'''

from itertools import groupby
weather = [{'date': '2019-12-15', 'weather': 'cloud'},
           {'date': '2019-12-13', 'weather': 'sunny'},
           {'date': '2019-12-14', 'weather': 'cloud'}]

# 分组前没有按照分组字段排序，分组失败
for k, item in groupby(weather, key=lambda x: x['weather']):
    print(k)
    for i in item:
        print(i)

print('******************************')

# 分组前按照分组字段排序，分组成功
weather.sort(key=lambda x: x['weather'])
for k, item in groupby(weather, key=lambda x: x['weather']):
    print(k)
    for i in item:
        print(i)
