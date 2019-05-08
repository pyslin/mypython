print(list(range(1,11)))


L = []
L = [x*x for x in range(1,11)]
print(L)

L2 = [x*x for x in range(1,11) if x%2==0]
print(L2)

L3 = [m+n for m in 'abc' for n in 'xyz']
print(L3)

import os
L4 = [d for d in os.listdir('.')]
print(L4)

d = {'x':'a','y':'b','z':'c'}
for k,v in d.items():
    print(k,'=',v)


d = {'x':'a','y':'b','z':'c'}
L5 = [k +'='+ v for k,v in d.items()]
print(L5)

L6 = ['HELLO','WORLD','IBM']
L7 = [s.lower() for s in L6]
print(L7)