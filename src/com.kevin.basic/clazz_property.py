# 面向对象高级编程 - @property

# 使用@property将方法变成属性
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100')
        self._score = value

s = Student()
s.score = 100
print(s.score)

# 使用@property定义只读属性
class People(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

