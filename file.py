import os
print(os.name)
#print(os.uname())
#没（）是变量
print(os.environ)
print(os.environ.get('path'))
print(os.environ.get('x','default'))

#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

## 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
#把两个路径合成一个时，不要直接拼字符串，
# 而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
#linux msos \    windows/
os.path.join('/Users/michael', 'testdir')

#创建一个目录make
os.mkdir('/Users/michael/testdir')

#删一个目录remove
os.rmdir('/Users/michael/testdir')

#拆分为路径和目录或文件
print(os.path.split('/Users/michael/test.txt'))

#拆分为路径加名  和 扩展名extension name
print(os.path.splitext('/Users/michael/test.txt'))

#合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

#当前目录下文件改名 删除
#os.rename('test.txt','test.py')
#os.remove('test.txt')



#使用os.unlink()和os.remove()来删除文件
#!/user/local/bin/python2.7
# -*- coding:utf-8 -*-

import os

my_file = 'C:/Users/michael/test4.txt'
if os.path.exists(my_file):
    #删除文件，可使用以下两种方法。
    os.remove(my_file)
    #os.unlink(my_file)
else:
    print('no such file:%s'%my_file)

      # x  for x在os。list当前目录   if是目录的
list = [x for x in os.listdir('.') if os.path.isdir(x)]
print(list)


print('####')
        #x      遍历当前目录           是否 是文件           把拆分为路径 名字  和扩展名 取第二个 是.py  不是py
#list2 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='py']
list2 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
list3 = [x for x in os.listdir('.')]

for x in list3:
    print(x)

print('!!!!')

#空格间隔
#for x in list2:
#   print(x,end = ' ')

for x in list2:
    print(x,end = ',')


"""
def func(L):
    for i in L:
        if (isinstance(i, [])):
            func(i)
            print('1')
        else:
            print('2')
            print(i)


func(list2)
func(list3)
"""