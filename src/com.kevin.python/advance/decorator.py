# 装饰器

import functools

# 装饰器就是返回函数的函数
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    print('2017-11-20')

now()

# 如果decorator本身需要传入参数，则需要编写一个返回decorator的函数
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("{} {}: ".format(text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-11-20')

now()

