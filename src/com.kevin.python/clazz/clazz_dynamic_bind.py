# 面向对象高级编程 - 动态绑定

class Student(object):
    pass

# 动态给实例绑定一个属性
s = Student()
s.name = 'Michael'
print(s.name)

# 动态给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 给所有实例绑定一个方法
def set_score(self, score):
    self.score = score

Student.set_score = set_score
s.set_score(100)
print(s.score)



