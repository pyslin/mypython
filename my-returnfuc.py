def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

#不需要立刻求和，可以不返回求和结果，而是返回求和函数
#内部函数可以引用外部参数和局部变量，返回函数sum时，相关参数保存在保存函数里，闭包closure
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print(f)
print(f())
#即使同样参数，返回的函数是不一样的，两个函数相互独立，调用结果互不影响
f2 = lazy_sum(1,3,5,7,9)
print(f == f2)


def count():
    fs = []
    for i in range (1,4):
        def fuc3():
            return i*i
        fs.append(fuc3)
    return fs
fuc11,fuc22,fuc33=count()
print(fuc11(),fuc22(),fuc33())
#每次循环，都创建一个函数，都引用变量i，并非立刻执行，都返回后i变为3
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量

