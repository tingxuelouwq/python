# 可变参数
def printInfo(name, *vartuple):
    print(name)
    for var in vartuple:
        print(var)
    return

printInfo('kevin', 'male', 25)