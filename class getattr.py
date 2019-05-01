class Student(object):
    def __init__(self):
        self.name = 'Bob'

    def __getattr__(self,attr):
        if attr == 'score':
            return 99
    def __getattr__(self,attr):
        if attr == 'age':
            return lambda:25
        raise AttributeError('\'Student\'object has no attribute \'%s\''%attr)
#只有在没有找到属性的情况下，才调用__getattr__，
# 已有的属性，比如name，不会在__getattr__中查找。
#要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误
s = Student()
print(s.fin)

class Chain(object):

    def __init__(self,path=''):
        self.__path = path

    def __getattr__(self,path):
        return Chain('%s%s'%(self.__path,path))
    def __atr__(self):
        return self.__path
    __repr__ = __str__
 Chain().status.user.timeline.list

