#!/usr/bin/python3

# 类定义
class People(object):
    # 定义公有属性
    name = ''
    age = 0
    # 定义私有属性
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    # 定义公有方法
    def speak(self):
        print('%s is %d years old.' % (self.name, self.age))

if __name__ == '__main__':
    p = People('kevin', 25, 60)
    p.speak()