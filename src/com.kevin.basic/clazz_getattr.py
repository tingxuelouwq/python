# 面向对象高级编程 - __getattr__

class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 100

s = Student()
print(s.name)
print(s.score)