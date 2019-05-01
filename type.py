print(type(123))
print(type('str'))
print(type(None))
print(type(abs))
print(type('abc')==str)

print(isinstance([1,2,3],(list,tuple)))
print(dir('abc'))
print(len('abc'))
print('abc'.__len__())

class Mydog(object):
    def __len__(self):
        return 100
dog = Mydog()
print(len(dog))
print('ABc'.lower())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.y
obj = MyObject()

#obj 有x属性吗
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(obj.y)
print('#####')
print(getattr(obj,'y'))
print(getattr(obj,'y',404))
#如果属性不存在，传入一个default参数，就返回默认值：
print(getattr(obj,'z',404))

#这些内置函数，只不知道对象信息的情况下才用

def readImage(fp):
    if hasattr(fp,'read'):
        return readData(fp)
    return None

