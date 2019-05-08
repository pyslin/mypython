#从environ变量里取出HTTP请求的信息,只是这么写下去代码是肯定没法维护了。
#让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做
"""
处理3个URL，分别是：

GET /：首页，返回Home；

GET /signin：登录页，显示登录表单；

POST /signin：处理登录表单，显示登录结果
同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。
lask通过Python的装饰器在内部自动地把URL和函数给关联起来
"""
from flask import Flask
from flask import request

my_webf = Flask(__name__)

@my_webf.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@my_webf.route('/signin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign in</button></p>
              </form>
              '''

@my_webf.route('/signin',methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello admin</h3>'
    else:
        return '<h3>Bad username or password.</h3>'

if __name__ =='__main__':
    my_webf.run()