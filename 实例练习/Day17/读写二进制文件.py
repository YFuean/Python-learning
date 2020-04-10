def main():
    try:
        # 将1bg4.jpg以二进制只读方式打开，读入data变量
        with open('./res/bg4.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))

        # 将bg4.jpg二进制写的方式打开，写入bg4.jpg_copy
        with open('./res/bg4.jpg', 'wb') as fs2:
            fs2.write(data)

    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)
    print('程序执行结束')


if __name__ == "__main__":
    main()
