from datetime import datetime
#datetime模块还包含一个datetime类
#如果仅导入import datetime，则必须引用全名datetime.datetime
#datetime.now()返回当前日期和时间，其类型是datetime
#datetime对象now（）方法可以返回当前时间的对象
now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015,4,19,12,20)
print(dt)

print(dt.timestamp())
t = 1429417200.0
#秒转化为当地时间
print(datetime.fromtimestamp(t))
#转化为格林威治时间
print(datetime.utcfromtimestamp(t))

cday = datetime.strtime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S')
print(cday)