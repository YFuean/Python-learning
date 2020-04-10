def main():
    str = '每个人身上都有太阳，主要是如何让它发光——苏格拉底'
    try:
        # w写入，如果文件存在，则写入，如果不存在，则创建
        f = open('./res/test.txt', 'w', encoding='utf-8')
        print(f.write(str))
        f.close

        # a写入，文件存在，则在文件内容后追加写入，如果不存在，则创建
        f = open('./res/test.txt', 'a', encoding='utf-8')
        print(f.write(str))
        f.close

        # with关键词系统会自动关闭文件和异常处理
        with open('./res/test.txt', 'w') as f:
            f.write(str)

    except IOError as e:
        print(e)
    print('写入完毕')


if __name__ == '__main__':
    main()
