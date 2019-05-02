#Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。
#在IO编程中，就存在速度严重不匹配的问题

#第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO
#一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，
# 于是，后续代码可以立刻接着执行，这种模式称为异步IO

#通知你的方法也各不相同。如果是服务员跑过来找到你，这是回调模式，
# 如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式

#现代操作系统不允许普通的程序直接操作磁盘
#读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符）
#通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）。

f = open('/Users/michael/test.txt','r')
print(f.read())
f.close

#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('/Users/michael/test.txt')
    print(f.read())
finally:
    if f:
        f.close()
#简洁版
with open('/Users/michael/test.txt') as f:
    print(f.read())

#可以反复调用read(size)方法，每次最多读取size个字节的内容。
#调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
with open('/Users/michael/test2.txt','r') as f:
    print('####')
    print(f.readline())
    print('###')
    #print(f.readlines())
    print('###')
    for line in f.readlines():
        print(line.strip())
        #把末尾\n去掉

#二进位打开'rb'
with open('/Users/michael/test.jpg','rb') as f:
    print(f.read())

#中文，encoding='gbk'
with open ('/Users/michael/test3.txt','r',encoding = 'gbk') as f:
    print(f.read())

#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError
#open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
with open('/Users/michael/test2.txt','r',encoding = 'gbk',errors = 'ignore') as f:
    for line in f.readlines():
        print(line.strip())

#传入标识符'w'或者'wb'表示写文本文件或写二进制文件
#可以传入'a'以追加（append）模式写入。
with open('/Users/michael/test.txt','w',encoding = 'gbk',errors = 'ignore') as f:
    f.write('你好')