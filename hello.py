#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__='Micheal Liu'

#让这个hello.py文件直接在Unix/Linux/Mac上运行
#第2行注释表示.py文件本身使用标准UTF-8编码
#任何模块代码第一个字符串视为模块的文档注释
import sys
#导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能
def test():
    args = sys.argv
#该。py的文件名hello.py
    if len(args)==1:
        print('Hello world')
    elif len(args)==2:
        print('Hello,%s!'%args[1])
    else:
        print('Too many arguments!')
if __name__=='__main__':
    test()
#命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
#如果在其他地方导入该hello模块时，if判断将失败

#_author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问
#_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等