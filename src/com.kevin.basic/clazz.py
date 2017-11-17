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
        print('%s is %d years old.' %(self.name, self.age))

# 单继承
class Student(People):
    grade = ''

    def __init__(self, name, age, weight, grade):
        # 调用父类的构造函数
        super(Student, self).__init__(name, age, weight)
        self.grade = grade

    # 覆写父类的方法
    def speak(self):
        print('%s is %d years old, and is grade %d.' %(self.name, self.age, self.grade))

# 另一个基类，用于多重继承
class Speaker(object):
    name = ''
    topic = ''

    def __init__(self, name, topic):
        self.name = name
        self.topic = topic


    def speak(self):
        print('%s is a speaker, and topic is %s.', self.name, self.topic)

# 多重继承
class Sample(Speaker, Student):
    def __init__(self, name, age, weight, grade, topic):



s = Student('kevin', 25, 65, 6)
s.speak()