# 面向对象高级编程 - __call__

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('my name is {}'.format(self.name))

s = Student('Kevin')
s()