"""
输入年份 如果是闰年输出true 否则输出false
Date:2020.3.25
Author:yuefan
"""

year = int(input("请输入年份："))

# 如果代码太长 可以用\对代码进行折行
is_leap = (year % 4 == 0 and year % 100 != 0) or \
    year % 400 == 0
print(is_leap)
