# 生成器

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

# 杨辉三角形
def pascal_triangle(line):
    i, arr = 0, [1]
    for n in range(line):
        print(arr)
        arr = [1] + [arr[i] + arr[i + 1] for i in range(0, len(arr) - 1)] + [1]

def pascal_triangle2(line):
    i, arr = 0, [1]
    for n in range(line):
        yield arr
        arr = [1] + [arr[i] + arr[i + 1] for i in range(0, len(arr) - 1)] + [1]

if __name__ == '__main__':
    print(__name__)
    fib(5)

    for arr in pascal_triangle2(2):
        print(arr)

