def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value:%s'%s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise
#raise语句如果不带参数，就会把当前错误原样抛出。
bar()