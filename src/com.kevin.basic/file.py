# 文件读写

filename = 'C:\\Users\\king\\Desktop\\书单.txt'
f = open(filename, 'rb+')

f.write(b'0123456789abcdef')
f.seek(-3, 2)
print(f.read(1))

f.close()


