# 斐波那契数列模块
def fib(n):
    print(__name__)
    count, a, b = 0, 0, 1
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count = count + 1
    print()

def fib2(n):
    print(__name__)
    count, a, b = 0, 0, 1
    while count < n:
        yield a
        a, b = b, a + b
        count = count + 1

if __name__ == '__main__':
    print(__name__)
    fib(5)