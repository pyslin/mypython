class Student(object):
    def __init__(self,name):
        self.name = name

print(Student('Bob'))

#类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
#该方法返回一个迭代对象
class Fib(object):
    def __init__(self):
#初始化两个参数ab
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
         self.a,self.b = self.b,self.a + self.b
         #退出循环条件
         if self.a > 100000:
             raise StopIteration()
         return self.a



for n in Fib():
    print(n)