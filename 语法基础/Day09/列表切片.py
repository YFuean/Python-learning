'''
列表切片
Author:zhent
'''
fruits = ['apple', 'grape', 'peach', 'strawberry', 'pear']
fruits += ['pitaya', 'mango', 'waxberry']
# 列表切片
fruits2 = fruits[1:4]
# ['grape', 'peach', 'strawberry']
print(fruits2)
# 可以通过完整切片操作直接复制过来
# ['apple', 'grape', 'peach', 'strawberry', 'pear','pitaya', 'mango', 'waxberry']
fruits3 = fruits[:]
print(fruits3)
# ['pitaya', 'mango']
fruits4 = fruits[-3:-1]
print(fruits4)
# 反向切换操作获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
# ['waxberry','mango', 'pitaya','pear','strawberry','peach','grape', 'apple']
print(fruits5)
