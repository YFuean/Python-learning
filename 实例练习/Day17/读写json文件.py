# json模块主要四个函数：
# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象
import json


def main():
    # 定义字典对象
    mydict = {
        'name': 'Tony.T',
        'age': 21,
        'qq': 1412666584,
        'friend': ['Snake.Y', 'Summer.X'],
        'lipstick': [
            {'brand': 'Chanel', 'color': '56 - ROUGE CHARNEL'},
            {'brand': 'perfectdiary', 'color': '810 葡萄美酒'},
            {'brand': '美康粉黛', 'color': '28#蓝田墨玉'}
        ]
    }
    try:
        # 将字典对象序列化到文件
        with open('./res/Tony.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')

    try:
        # 从文件中读入，反序列化成对象
        with open('./res/Tony.json', 'r', encoding='utf-8') as fs:
            mydict = json.load(fs)
            print(mydict)

    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    print('保存数据完成')


if __name__ == '__main__':
    main()
