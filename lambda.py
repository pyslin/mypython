list1 = list(map(lambda x:x*x,[1,2,3,4,5]))
print(list1)

def f(x):
    return x*x

fuc = lambda x:x*x
print(fuc)
print(fuc(5))
print('%%%')
def build(x,y):
    return lambda:x*x+y*y

fuc2 = build(1,2)
print(fuc2())

