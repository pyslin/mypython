#类定义暴露属性会被随意更改，set get方法可以限制也可以检查参数，略复杂。用装饰器@property
#”__“两个下划线，那么这个函数或变量就是私有的了。

#@property 把方法『变成』了属性。
class Student(object):
#相当于get方法，return来的
    @property
    def score(self):
        return self.__score
#相当于set方法
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must bu an integer')
        if value < 0 or value>100:
            raise ValueError('score must between 0-100')
        self.__score = value

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self,value):
        self.birth = value
#只定义getter方法，不定义setter方法就是一个只读属性
    @property
    def age(self):
        return 2015 - self.__birth

