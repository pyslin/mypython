#动态语言可以给实例绑定属性和方法
class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

def set_age(self,age):
    self.age = age

from types import MethodType
#对象。要用的方法名 = MethodType(方法名，对象）
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)


#绑定的方法别的对象不起作用
#s2 = Student()
#s2.set_age(30)

#给类绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score

class Student(object):
#用tuple定义可以绑定的属性,仅对当前有效，子类无效
#子类也加__slots__  限定于父类子类加起来
    __slots__ = ('name','age')

s = Student()
s.name = 'Bob'
s.age = 25
s.score = 89

class GrandStudent(Student):
    pass

g = GrandStudent()
g.score = 79
