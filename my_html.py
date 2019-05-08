"""
<html>

<head>
  <title>Hello</title>
  #CSS是Cascading Style Sheets（层叠样式表）的简称，CSS用来控制HTML里的所有元素如何展现
  #给标题元素加一个<h1>样式
  <style>
   h1 {
      color: #333333;
      font-size: 48px;
      text-shadow: 3px 3px 3px #666666;
    }
    </style>
    #JavaScript是为了让HTML具有交互性而作为脚本语言添加的
     <script>
    function change() {
      document.getElementsByTagName('h1')[0].style.color = '#ff0000';
    }
  </script>
</head>

<body>

   <h1 onclick="change()">Hello, world!</h1>
</body>

</html>
"""
"""
我们其实就明白了一个Web应用的本质就是：

1.浏览器发送一个HTTP请求；

2.服务器收到请求，生成一个HTML文档；

3.服务器把HTML文档作为HTTP响应的Body发送给浏览器；

4.浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。
因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。

这个接口就是WSGI：Web Server Gateway Interface。
WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
    
    environ：一个包含所有HTTP请求信息的dict对象
    start_response：一个发送HTTP响应的函数
    start_response()函数接收两个参数，一个是HTTP响应码，
    一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示
    我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过start_response()发送Header，最后返回Body
    
"""
def application(environ,star_response):
    star_response('200 OK',[('Content-Type','text/html')])
    #body = '<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]