# python没有块级作用域
if True:
    msg = 'hello world'
print(msg)

# 内部作用域可以使用global关键字修改全局作用域变量
num = 1
def fun1():
    global num
    print(num)  # 1
    num = 123
    print(num)  # 123
    return
fun1()
print(num)  # 123

# 内部作用域可以使用nonlocal关键字修改嵌套作用域变量
def outer():
    num = 10
    def inner():
        nonlocal num
        print(num)  # 10
        num = 100
        print(num)  # 100
        pass
    inner()
    print(num)  # 100
    pass
outer()