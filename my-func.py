print(abs(-10))
print(abs)
#abs(10)函数的调用 ，abs是函数
x = abs(10)
#要获得函数调用结果，可以把结果赋值给变量
print(x)
f = abs
#函数本身也可以赋值给变量，变量指向函数,函数名就是指向函数的变量
print(f(-5))

def add(x,y,f):
    return f(x)+f(y)
print(add(5,-6,abs))

def f(x):
    return x*x
r = map(f,[1,2,3,4,5])
#map会返回一个惰性iterator，用list（）函数把序列计算出来并返回list
print(list(r))

r2 = list(map(str,[1,2,3,4,5]))
#转换为字符返回惰性生成器，list（函数计算出来返回list
print(r2)
from functools import reduce
def add(x,y):
    return x + y
z = reduce(add,[1,2,3,4,5])
print(z)

def fn(x,y):
    return x*10+y
z2 = reduce(fn,[1,3,5,7,9])
print(z2)

def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

z3 = reduce(fn,map(char2num,'123456'))
print(z3)