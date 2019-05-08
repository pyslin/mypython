class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson',89)
print(bart)
print(Student)

print(bart.name)
bart.print_score()
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
#调用时，不用传递该参数

print(bart.get_grade())

class Student1(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
#set 方法可以实现对参数检查，避免传入无效的参数
    def set_score(self,score):
        if 0 <= score <= 100 :
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
#属性的名称前加上两个下划线__,只有内部可以访问，外部不能访问
#前后都是双下划线是特殊变量名

student1 = Student1('Bob',89)
print(student1.get_name())
#不能直接设置__name参数
student1.__name = 'new name'
print(student1.get_name())
