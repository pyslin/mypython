#{}dict []list ()tuple
#坐标可以表示为 p =(1,2),但不够明白，用定义类又大题小做

from collections import namedtuple,deque
#namedtuple是一个函数,可以快速定义tuple对象
Point = namedtuple('Point',['x','y'])
p =Point(1,2)
print(p.x)

# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])


q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)
#append() pop()  还支持appendleft() popleft(),快速双向插入和删除

#使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
#函数在创建defaultdict对象时传入,lambda:N/A匿名函数只返回N/A给对象
#却不能直接给N/A，因为对象的参数是一个函数类型
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print(dd['key2'])

#OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict

od = OrderedDict()
od['z'] = 100
od['y'] = 10
print(list(od.keys()))

#Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c = Counter()
for char in 'programming':
    c[char] =c[char] + 1

print(c)

c = Counter()  # 创建一个空的Counter类
print(c)
c = Counter('gallahad')  # 从一个可iterable对象（list、tuple、dict、字符串等）创建
print(c)
c = Counter({'a': 4, 'b': 2})  # 从一个字典对象创建
print(c)
c = Counter(a=4, b=2)  # 从一组键值对创建
print(c)