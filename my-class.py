std1 = {'name':'Michael','score':98}
std2 = {'name':'Bob','score':81}
def print_score(std):
    print('%s:%s'%std['name'],std['score'])

#Student这种数据类型应该被视为一个对象,这个对象拥有name和score这两个属性（Property）
class Student(object):
#initialization初始化
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s'%(self.name,self.score))

bart = Student('Bart Simpson',59)
lisa = Student('Lisa simpson',87)
bart.print_score()
lisa.print_score()
#面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。
#类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”
# 每个对象都拥有相同的方法，但各自的数据可能不同
