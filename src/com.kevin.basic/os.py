import os

# 在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出绝对路径
def search(name, list=None, dirpath=None):
    if list is None:
        list = []
    if dirpath is None:
        dirpath = os.getcwd()

    for x in os.listdir(dirpath):
        abx = os.path.join(dirpath, x)
        if os.path.isdir(abx):
            search(name, list, abx)
        if os.path.isfile(abx) and name in x:
            list.append(abx)
    return list

list = search('test', dirpath='D:\\multithread')
for x in list:
    print(x)