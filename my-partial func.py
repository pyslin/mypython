print(int('12345'))
#默认十进位，可以参数base改为8进位
print(int('12345',base=8))

#大量转换时都要传参数麻烦，我们定义新函数
def int2(x,base=2):
    return int (x,base)

print(int2('1000000'))
#相当于调整默认参数，返回新函数
import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))

#创建偏函数实际接收了 函数对象，*args（默认值） **kw（参数）
#int2（"100")相当于 int， *args ，base=2
max2 = functools.partial(max,10)
print(max2(2,3,4))
#max2 相当于 max ；10，2，3，4；**kw