# 使用元类实现ORM框架

# Field类，负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '{}:{}'.format(self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')


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
            if isinstance(v, Field):
                print('Found mapping: {} ==> {}'.format(k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings    # 保存属性和列的映射关系
        attrs['__table__'] = name     # 假设表名和类名一致

        return super().__new__(cls, name, bases, attrs)


# Model
class Model(dict, metaclass=ModelMetaClass):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into {}({}) values({})'.format(self.__table__, ','.join(fields), ','.join(params))
        print('SQL: {}'.format(sql))
        print('ARGS: {}'.format(args))


class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

