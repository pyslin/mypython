#Web框架把我们从WSGI中拯救出来了。现在，我们只需要不断地编写函数，带上URL，就可以继续Web App的开发了
#在函数中返回一个包含HTML的字符串，简单的页面还可以，
# 但是，想想新浪首页的6000多行的HTML，你确信能在Python的字符串中正确地写出来么？
#使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和指令，
# 然后，根据我们传入的数据，替换后，得到最终的HTML，发送给用户：
"""
这就是传说中的MVC：Model-View-Controller，中文名“模型-视图-控制器”。

Python处理URL的函数就是C：Controller，Controller负责业务逻辑，比如检查用户名是否存在，取出用户信息等等；

包含变量{{ name }}的模板就是V：View，View负责显示逻辑，通过简单地替换一些变量，View最终输出的就是用户看到的HTML。

MVC中的Model在哪？Model是用来传给View的，这样View在替换变量的时候，就可以从Model中取出相应的数据。
Flask通过render_template()函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2
"""
from flask import Flask,request,render_template

my_webf2 = Flask(__name__)

@my_webf2.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@my_webf2.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

@my_webf2.route('/signin',methods=['post'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html',username=username)
    else:
        return render_template('form.html',message='Bad username or password',username=username)

if __name__ =='__main__':
    my_webf2.run()


"""通过MVC，我们在Python代码中处理M：Model和C：Controller，而V：View是通过模板处理的，
这样，我们就成功地把Python代码和HTML代码最大限度地分离了。"""
#在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。
# 很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令
"""
循环输出页码：
{% for i in page_list %}
    <a href="/page/{{ i }}">{{ i }}</a>
{% endfor %}

除了Jinja2，常见的模板还有：

Mako：用<% ... %>和${xxx}的一个模板；

Cheetah：也是用<% ... %>和${xxx}的一个模板；

Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。
有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。


"""