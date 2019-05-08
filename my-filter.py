def is_odd(n):
    return n%2 == 1
list1 = list(filter(is_odd,[1,2,3,4,5]))
print(list1)

def not_empty(s):
    return  s
#
list2 = list(filter(not_empty,['a','','   ',None,'c']))
print(list2)

def not_empty(s):
    return  s and s.strip()
#根据返回值是true还是false再决定留不留s
#两个空格是true 就会留着，所以还要通过strip（）去除空格/n/t后还是true，才能留着
#如果单独s.strip（），none就会出错，但用and就可以前面一个就是false，不用判断后面一个了
list2 = list(filter(not_empty,['a','','   ',None,'c']))
print(list2)
print('###')
#构造从2开始的无穷大自然数列
#def _odd_iter():
#    n = 2
 #   while True:
#        yield n
 #       n = n + 1
#也可以n=1，n=n+2的3开始的奇数序列，偶数肯定不是素数
def _odd_iter():
     n = 1
     while True:
        n = n + 2
        yield n


#筛，取余大于0的数
def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
#初始化序列
    it = _odd_iter()
    yield 2
    while True :
#返回数列第一个数
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

i=1
for n in primes():
    if n < 1000:
        print(i,':',n)
        i = i + 1
    else:
        break