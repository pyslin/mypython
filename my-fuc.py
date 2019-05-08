# -*- coding: utf-8 -*-
def my_abs(x):
    if x>=0 :
        return x
    else:
        return -x

print(my_abs(-80))

def nop() :
    pass
age = 20
if age>18:
    pass


import math

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.cos(angle)
    return nx, ny

x,y = move(100,40,60,math.pi/6)
print(x,y)

r = move(100,40,60,math.pi/6)
print(r)

def power( x,n=2):
    s=1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5,3))

def enroll(name,gender, age = 6,city = 'Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city:',city)

enroll('Sarah','F')
enroll('Tom','M',7)
enroll('Eric','F',city = 'Nanjing')


def add_end(L=[]):
    L.append('END')
    return L

L=add_end([1,2,3])
for x in L:
    print(x)
print('______')

L=add_end(['x','y'])
for x in L:
    print(x)

print('******')
L=add_end()
for x in L:
    print(x)

print('&&&&&&&')
L=add_end()
for x in L:
    print(x)

print('&&&&&&&')

def add_end1(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

add_end1()
for x in L:
    print(x)
