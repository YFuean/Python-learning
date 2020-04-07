'''
元组类型练习
'''
# 定义元组
t = ('猪猪', 12, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[2])
# 遍历元组中的值
for number in t:
    print(number)

# 重新给元组赋值
t = ('王大锤', 20, True, '云南昆明')
print(t)
# 将元组转化成列表
person = list(t)
print(person)
# 列表可以修改元素
person[0] = '李云龙'
person[1] = 50
print(person)
# 将列表转换成元组
fruit_list = ['apple', 'banana', 'orange']
fruit_tuple = tuple(fruit_list)
print(fruit_tuple)
