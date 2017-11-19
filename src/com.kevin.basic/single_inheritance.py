from clazz import People


# 单继承
class Student(People):
    grade = ''

    def __init__(self, name, age, weight, grade):
        # 调用父类的构造函数
        super(Student, self).__init__(name, age, weight)    # Python3可使用super.__init__(...)
        self.grade = grade

    # 覆写父类的方法
    def speak(self):
        print('%s is %d years old, and is grade %d.' % (self.name, self.age, self.grade))


if __name__ == '__main__':
    s = Student('kevin', 25, 65, 6)
    s.speak()
