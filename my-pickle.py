import pickle
d = dict(name='bob',age=20,score=88)
#可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。
#pickle.dumps()方法把任意对象序列化成一个bytes
f = open('dump.txt','wb')
#一个带s
pickle.dumps(d)
pickle.dump(d,f)
f.close

with open('dump.txt','rb') as  f:
    d = pickle.load(f)
    print(d)

#只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

#json转换可以各个语言传输
import json
d = dict(name='bob',age=20,score=88)
print(json.dumps(d))
#很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化

print('####')

import json

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
#dumps()方法不知道如何将Student实例变为一个JSON的{}对象
#我们只需要为Student专门写一个返回｛｝的转换函数，再把函数作为参数传进去即可
def Student2dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
s = Student('Bob',20,88)
print(json.dumps(s,default=Student2dict))
print('@@@')

#class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
#print(json.dumps(s,default=lambda obj:obj.__dict__))

#如果我们要把JSON反序列化为一个Student对象实例
#loads()方法首先转换出一个dict对象
# 我们传入的object_hook函数负责把dict转换为Student实例
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])


json_str = '{"age":20,"score":88,"name":"bob"}'
print(json.loads(json_str,object_hook=dict2student))