#数据读写不一定是文件，也可以在内存中读写。
#要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

from io import StringIO
#都是大写IO
f = StringIO()
#f = StringIO()
f.write('Hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

from io import StringIO
#f指向open stringIO的对象
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
#对这个对象可以readline
    s = f.readline()
#出现空要break出来
    if s == '':
        break
#去除\n
    print(s.strip())


#tringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO
#f = BytesIO()
#f.write('中文'.encode('utf-8'))
f = BytesIO('中文'.encode('utf-8'))
print(f.getvalue())

#请注意，写入的不是str，而是经过UTF-8编码的bytes。