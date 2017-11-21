# 面向对象编程 - __getitem__

class Fib(object):
    def __getitem__(self, n):
        a, b = 0, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print(f[3])