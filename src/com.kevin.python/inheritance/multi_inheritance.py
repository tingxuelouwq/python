from single_inheritance import Student

# 类定义
class Speaker(object):
    name = ''
    topic = ''

    def __init__(self, name, topic):
        self.name = name
        self.topic = topic

    def speak(self):
        print('%s is a speaker, and topic is %s.' % (self.name, self.topic))

# 多重继承
class Sample(Speaker, Student):
    def __init__(self, name, age, weight, grade, topic):
        Speaker.__init__(self, name, topic)
        Student.__init__(self, name, age, weight, grade)

s = Sample('kevin', 25, 65, 6, 'Python')
s.speak()
print(Sample.mro())