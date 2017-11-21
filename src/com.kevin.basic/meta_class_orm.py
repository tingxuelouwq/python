# 使用元类实现ORM框架

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()Field

# Field类，负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '{}:{}'.format(self.__class__.__name__, self.name)


# StringField类
class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')


# InegerField类
class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'bigint')


# ModelMetaClass
class ModelMetaClass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return super().__new__(cls, name, bases, attrs)
        print('Found model: {}'.format(name))

        mappings = dict()
        for k, v in attrs.items():


# Model
class Model(dict, metaclass=ModelMetaClass):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise
