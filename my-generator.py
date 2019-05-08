L = [x*x for x in range(10)]
print(L)
g = (x*x for x in range(10))
print(g)
print(next(g))
print(next(g))
print("@@@@")
for n in g :
    print(n)


def fib(max):
    n,a,b = 0,0,1
    while n<max:
        print(b)
        temp = b
        b = a + b
        a = temp
        n = n + 1
    return'done'

print(fib(6))
print('$$$$')

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib2(6))


def odd():
    print('step1')
    yield(1)
    print('step2')
    yield(3)
    print('step3')
    yield(5)

o = odd()
next(o)
print('****')
next(o)
print('%%%%')
print(o)
next(o)
print(o)
print('@@@')

def fibkk(max):
    n,a,b = 0,0,1
    while n <max:
        yield b
        a,b = b,a+b
        n = n + 1
        return 'done'

for n in fibkk(6):
    print(n)

g = fibkk(6)
while True:
    try:
        x = next(g)
        print('g',x)
    except StopAsyncIteration as e:
        print('Generator return value:',e.value)
        break