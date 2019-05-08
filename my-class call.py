class Student(object):
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print('My name is %s' %self.name)

s = Student('Bob')
print(s())
#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样
#全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
print(callable(Student('Bob')))
print(callable(max))
print(callable('asd'))