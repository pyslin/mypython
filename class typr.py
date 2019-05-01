class Hello(object):
    def hello(self,name='world'):
        print('Hello,%s'%name)

h = Hello()
print(h.hello())

print(type(Hello))
#Hllo是一种数据类型，h是定义的一个数据

def fn(self,name='world'):
    print('Hello,%s'%name)

Helloworld = type('Helloworld',(object,),dict(helloworld=fn))
#要创建一个class对象，type()函数依次传入3个参数：
# 1class的名称；
#继承的父类集合，注意Python支持多重继承，
# 如果只有一个父类，别忘了tuple的单元素写法；
#class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上

h1 = Helloworld()
print(h1.helloworld())

#使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass元类
#先定义metaclass，就可以创建类，最后创建实例。
#metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
