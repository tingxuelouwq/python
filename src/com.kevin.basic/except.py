# 异常处理
import sys

# try...exception...finally
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('Os error: {0}'.format(err))
except ValueError:
    print('Could not convert data to an integer.')
except(RuntimeError, TypeError, NameError):    # 一个except子句可以同时处理多个异常
    pass
except:    # 最后一个except子句可以忽略异常名称，当做通配符使用
    print('Unexpected error: ', sys.exc_info()[0])
    raise    # 继续抛出异常
finally:
    print('executing finally clause')

# 自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2 * 2)
except MyError as e:
    print('My exception occurred, value: ', e)
