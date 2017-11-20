# 文件读写
filename = 'C:\\Users\\king\\Desktop\\书单.txt'
f = open(filename, 'wb+')

f.write(b'0123456789abcdef')
f.seek(-3, 2)
print(f.read(1))

f.close()

# 内存写str
from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# 内存读str
f = StringIO('hello\nHi\nGoodbye')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# 内存写bytes
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 内存读bytes
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
bytes = f.read()
print(bytes)


