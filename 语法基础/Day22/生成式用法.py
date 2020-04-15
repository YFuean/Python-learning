'''
生成式用法
生成式（推导式）可以用来生成列表、集合、字典
'''
import os

# 列表生成式生成自然数序列
list1 = list(range(1, 11))
print(list1)

# 列表生成式生成自然数平方序列
list2 = [x*x for x in range(1, 11)]
print(list2)

# 可以带条件
list3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(list3)

# 列出指定目录下所有文件和目录名
list4 = [d for d in os.listdir('./res')]
print(list4)

# 结合两个列表的不相等元素
list5 = [(x, y) for x in [1, 2, 3] for y in [2, 3, 4]]
print(list5)

# 字典生成式
score = {
    'Tony': 60,
    'Arthur': 74,
    'John': 56,
    'Alexander': 97,
    'Justin': 84,
    'Taylor': 34,
    'Elizabeth': 63
}
score1 = {key: value for key, value in score.items() if value >= 60}
print(score1)
