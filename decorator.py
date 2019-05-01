def now():
    print('2015-3-25')

func1 = now
print(func1())
#双下划线，一个属性
print(now.__name__)
print(func1.__name__)
#现在想动态增加now的功能，但不改now函数的定义，装饰器
print('*****')
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print('2015-1')
#把@log放now（）函数定义处，相当于执行now =log（now）
#lod返回函数，原来now（）还在，只是现在同名的now变量指向了新的函数
## 调用now（）执行新函数即log（）返回的wrapper（）

print(now())
print(now.__name__)
#now的固有name已经变为wrapper了
print('!!!')
#如果装饰器需传入参数，就要编写一个返回装饰器的高阶函数

import functools
def log(text):
    def decorator(func):
        # wraps 包装，即用now名字包装一下wrapper函数
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s%s()'%(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

#相当于now = log（‘execute’）（now）
@log ('execute')
def now1():
    print('2016-1')

print(now1())
print(now1.__name__)
