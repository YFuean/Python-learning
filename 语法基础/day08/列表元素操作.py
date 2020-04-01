'''
列表元素添加和删除
'''

list1 = [1, 2, 3, 4, 5, 6]
list1.append(100)
list1.insert(1, 400)
print(list1)
# 合并两个列表
list1.extend([11, 22, 33])
print(list1)
print(len(list1))
# 先通过成员运算判断元素是否在列表中，如果存在就删除元素
if 100 in list1:
    list1.remove(100)
if 1234 in list1:
    list1.remove(1234)
print(list1)
# 从指定的位置删除元素
list1.pop(0)
list1.pop(len(list1)-1)
print(list1)
# 清空元素
list1.clear
print(list1)
