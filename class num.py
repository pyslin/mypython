JAN = 1
FEB = 2
#好处是简单，缺点是类型是int，并且仍然是变量。
#更好的方法是为这样的枚举类型定义一个class类型
#每个常量都是class的一个唯一实例

from enum import Enum
Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

#month 类里有个month.__member__的tuple
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

#value属性则是自动赋给成员的int常量，默认从1开始计数。
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import Enum,unique
#@unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday.Tue.value)

print(Weekday(1))