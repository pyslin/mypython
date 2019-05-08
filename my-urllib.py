#urllib的request模块可以非常方便地抓取URL内容，
# 也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
#url 的library
#urllib.request可以用来发送request和获取request的结果
#urllib.error包含了urllib.request产生的异常
#urllib.parse用来解析和处理URL
#urllib.robotparse用来解析页面的robots.txt文件


from urllib import request
#urllib包request模块   request类 urlopen（）方法
url = 'http://www.baidu.com'
header = {
   'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
#实例化一个Reuest对象
req = request.Request(url,headers=header)

#对象传入urlopen函数
#使用urllib.request.urlopen()返回的对象是一个http.client.HTTPResponse类型的对象，
# 它主要包含的方法有read(),readinto(),getheader(name),getheaders(),fileno()等函数
# 和msg,version、status,reason,debuglevel,closed等属性。
with request.urlopen(req) as f:
#就有status reason等参数，getheaders（）。read（）等函数
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('###')
    print('Data:', f.read().decode('utf-8'))

#fhandle = open("./1.html","wb")
#fhandle.write(f.read())
#fhandle.close()


