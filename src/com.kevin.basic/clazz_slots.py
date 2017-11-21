# 面向对象高级编程 - __slots__

# __slots__用于指定可以绑定的属性
class Student(object):
    __slots__ = ('name', 'age')
    pass

s = Student()
s.name = 'kevin'
s.age = 25
# s.score = 100   # AttributeError: 'Student' object has no attribute 'score'

# __slots__仅对当前类实例起作用，对子类不起作用
# 除非子类也使用__slots__，则此时子类实例允许绑定的属性就是自身的__slots__加上父类的__slots__
class GraduateStudent(Student):
    __slots__ = ('score')
    pass

g = GraduateStudent()
g.name = 'tom'
g.score = 100
print(g)