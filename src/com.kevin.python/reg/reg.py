import re

# re.match()
line = 'Cats are smarter than dogs'

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
    print('matchObj.groups(): ', matchObj.groups())
    print('matchObj.group(1): ', matchObj.group(1))
    print('matchObj.group(2): ', matchObj.group(2))


# re.search()
print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())


# re.split()
print(re.split(r'\s+', 'a b  c'))


# re.sub()
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码: ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码: ", num)


# re.compile()
# 编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-65538').groups())