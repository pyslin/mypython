#把一个表的内容用Python的数据结构表示出来的话，
# 可以用一个list表示多行，list的每一个元素是tuple，表示一行记录
"""
[
    ('1','Michael'),
    ('2','Bob'),
    ('3','Adam')
]

class User(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name

[
    User('1','Michael'),
    User('2','Bob'),
    User('3','Adam')

]
"""
#这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上
#是由谁来做这个转换呢？所以ORM框架应运而生
#在Python中，最有名的ORM框架是SQLAlchemy。

#from sqlalchemy import Column,String,creat_engine
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#创建基类
Base = declarative_base()
print(type(Base))

#继承基类
class User(Base):
    __tablename__='user'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

# 初始化数据库连接参数
#engine = create_engine('mysql+mysqlconnector: //root:password@localhost:3306/test')
#engine = create_engine('mysql+mysqlconnector://<root>:<password>@<127.0.0.1>[:3306]/<test>')
engine = create_engine('mysql://root:password@localhost:3306/test')
#实例化sessionmaker bind绑定参数
DBSession = sessionmaker(bind=engine)

