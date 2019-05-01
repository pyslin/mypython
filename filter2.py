#构造从2开始的序列
def _odd_iter():
    n = 2
    while True:
        yield n
        n = n + 1


#构造取余大于0的筛
def _not_divisible(n):
    return lambda x: x % n > 0


def primes():

    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        #筛掉除尽n的数
        it = filter(_not_divisible(n), it) # 构造新序列

# 打印1000以内的素数:
i=1
for n in primes():
    if n < 1000:
        print(i,n)
        i=i+1
    else:
        break