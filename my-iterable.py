#from collections import Iterable

from collections.abc import Iterable,Iterator
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))
print(isinstance((x for x in range(10)),Iterator))
print(isinstance('abc',Iterator))

for x in [1,2,3,4,5]:
    print(x)
print('####')
it = iter([1,2,3,4,5])
while True :
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
