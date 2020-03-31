"""
字符串常用方法的练习
"""


def main():
    str1 = "Hello Python"
    # 通过内置函数len计算字符串的长度
    print(len(str1))
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())
    # 获得字符串首字母大写的拷贝
    print(str1.title())
    # 获得字符串首字母变大写的拷贝
    print(str1.upper())
    # 从字符串中查找子串所在的位置
    print(str1.find('or'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))
    print(str1.startswith('He1'))
    # 检查字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))
    str2 = "zhent1106@163.com"
    # 检查字符串的是否由数字构成
    print(str2.isdigit())
    # 检查字符串是否以字母构成
    print(str2.isalpha())
    # 检查字符串是以字母数字构成
    print(str2.isalnum())
    str3 = "zhent1106@163.com"
    print(str3)
    # 获得字符串修建左右两侧空格之后的拷贝
    print(str3.strip())


if __name__ == '__main__':
    main()
