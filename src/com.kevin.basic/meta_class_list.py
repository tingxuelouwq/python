# 使用元类，为list增加add()方法

# 自定义元类
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return super().__new__(cls, name, bases, attrs)

# mataclass关键字用于指定元类，元类的类名总是以Metaclass结尾
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)

