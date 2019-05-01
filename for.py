names = ['Michael','Tom','Eric']
for name in names:
    print(name)

sum1= 0
for x in [1,2,3,4,5,6,7,8,9]:
    sum1 = sum1 + x
print(sum1)


sum2 = 0
for x in range(101):
    sum2 = sum2 + x
print(sum2)

sum3 = 0
n = 1
while n<100:
    sum3= sum3 + n
    n = n + 2
print(sum3)

n = 1
while n < 101:
    if n > 10:
        break
    print(n)
    n = n +1
print('end')
print('_______________________')
n = 0
while n < 20:
    n = n + 1
    if n%2 == 0:
        continue
    print(n)



