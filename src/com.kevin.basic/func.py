# 可变参数
def print_info(name, *vartuple):
    print(name)
    for var in vartuple:
        print(var)
    return

print_info('kevin', 'male', 25)

# 匿名函数
sum = lambda num1, num2: num1 + num2
print(sum(1, 3))