'''
生成斐波那契数列的前20个
'''
x = 1
y = 1
z = 0
print(x, ',', y, end='')
for i in range(3, 21):
    # 第三项是两项之和
    z = x+y
    print(',', z, end='')
    # 前两项重新赋值
    x = y
    y = z
print()
