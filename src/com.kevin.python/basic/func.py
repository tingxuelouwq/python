# 可变参数
from functools import reduce

def print_info(name, *vartuple):
    print(name)
    for var in vartuple:
        print(var)
    return

print_info('kevin', 'male', 25)

# 匿名函数
sum = lambda num1, num2: num1 + num2
print(sum(1, 3))

# map()
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4])
print(list(r))

# reduce()
def add(x, y):
    return x + y

r = reduce(add, [1, 3, 5, 7, 9])
print(r)

# 使用map-reduce实现str2int
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))

# filter()
def not_empty(s):
    return s and s.strip()

r = filter(not_empty, ['A', '', 'B', None, 'C', '   '])
print(list(r))

# sorted()
l = sorted([36, 5, -12, 9, -21], key=abs)
print(l)