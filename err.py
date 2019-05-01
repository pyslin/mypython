# err.py:
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('1')
    except Exception as e:
        logging.exception(e)

main()
print('END')

#就可以把错误堆栈打印出来
#Python内置的logging模块可以非常容易地记录错误信息

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0 :
        raise FooError('invalid value:%s'%s)
    return(10 / n)

foo('0')
#只有在必要的时候才定义我们自己的错误类型。
#尽量使用Python内置的错误类型。