# 类与对象


class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def eat(self):
        if self.age < 18:
            print('%s只能吃儿童餐.' % self.name)
        else:
            print('%s可以吃成人餐.' % self.name)


def main():
    stu1 = Student('小明', 21)
    stu1.study('Python')
    stu1.eat()
    stu2 = Student('小刚', 17)
    stu2.eat()


if __name__ == '__main__':
    main()
