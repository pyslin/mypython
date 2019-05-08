def foo(s):
    n = int(s)
#凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
# print('>>>n = %d'% n)
    assert n != 0,'n is zero!'
    return 10 / n

def main():
    foo('0')

main()
#运行程序启动Python解释器时可以用-O参数来关闭assert

