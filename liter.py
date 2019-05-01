#切片
d = {'a':1,'b':2,'c':3}
for key in d :
    print(key)
for value in d.values():
    print(value)


from collections.abc import Iterable
#import Iterable from collections
print("#####")
print(isinstance('abc',Iterable))
for ch in 'abc':
    print(ch)


for i ,value in enumerate(['a','b','c']):
    print(i,value)
    
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)