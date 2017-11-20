'''
使用pickle模块进行序列化和反序列化
'''
#
# # 序列化
# import pickle
#
# # 使用pickle模块将数据对象保存到文件
# data = {
#     'a': [1, 2.0, 3, 4+6j],
#     'b': ('string', u'Unicode string'),
#     'c': None
# }
#
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
#
# output = open('C:\\Users\Kevin\Desktop\\test.txt', 'wb')
#
# pickle.dump(data, output)
# pickle.dump(selfref_list, output, -1)
#
# output.close()
#
# # 使用pickle模块从文件中重构python对象
# import pprint
#
# f = open('C:\\Users\\Kevin\\Desktop\\test.txt', 'rb')
#
# data1 = pickle.load(f)
# pprint.pprint(data1)
#
# data2 = pickle.load(f)
# pprint.pprint(data2)
#
# f.close()

'''
使用json模块进行序列化和反序列化
'''
import json

# 序列化
d = dict(name='Kevin', age=25, score=150)
json_str = json.dumps(d)
print(json_str)

# 反序列化
json_str = '{"name": "Kevin", "age": 25, "score": 150}'
d1 = json.loads(json_str)
print(d1)

# 序列化复杂对象
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# 写一个转换函数，将Student转换为dict
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
# 使用转换函数将Student转换为dict，进而转换为json字符串
print(json.dumps(s, default=student2dict))
# class实例通常都有一个__dict__属性，存储了实例的dict表示
print(json.dumps(s, default=lambda obj: obj.__dict__))

# 反序列化复杂对象
# 写一个转换函数，将dict转换为Student对象
def dict2sutdent(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"name": "Bob", "age": 20, "score": 88}'
# 使用转换函数将dict转换为Student
print(json.loads(json_str, object_hook=dict2sutdent))