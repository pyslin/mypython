def f(n):
    if n==1:
        return 1
    return n*f(n-1)

print('n!',f(5))


L = []
n = 1
while n<=99:
    L.append(n)
    n = n + 2

for x in L:
    print(x)
