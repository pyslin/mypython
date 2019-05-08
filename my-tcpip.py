#网络通信是两台计算机上的两个进程之间的通信。
#，IP地址对应的实际上是计算机的网络接口
#IP地址实际上是一个32位整数（称为IPv4），以字符串表示的IP地址如192.168.0.1
# 实际上是把32位整数按8位分组后的数字表示，目的是便于阅读
#CP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，
# 如果包丢掉了，就自动重发
#许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等。
#一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口
#一个TCP报文来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。每个网络程序都向操作系统申请唯一的端口号，

#Socket是网络编程的一个抽象概念。通常我们用一个Socket表示“打开了一个网络链接”，
# 而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可。

import socket

#AF_INET指定使用IPv4协议,如果要用更先进的IPv6，就指定为AF_INET6
#SOCK_STREAM指定使用面向流的TCP协议
#建立连接,是一个对象
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(type(s))
s.connect(('www.baidu.com',80))#两个括号，里面是tuple

#发送数据
#CP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定。
# ，HTTP协议规定客户端必须先发请求给服务器，服务器收到后才发数据给客户端。
#\r就是"回到行首"，\n就是"到下一行"
#即:\r是回车，\n是换行，前者使光标到行首，后者使光标下移一格。
#通常用的Enter是两个加起来的，即\r\n
#这些是报头分行，隔两行后是正文
#s.send(b'GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
s.send(b'GET / HTTP/1.1\r\nHost:www.baidu.com\r\nConnection: close\r\n\r\n')

#接收数据
buffer = []
while True:
    #调用recv（max）每次最多接收1024字节，放入buffer【】
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
#b''是一个空字节
#join是连接列表的函数
#buffer是一个字节串的列表
#连起来的意思就是使用空字节把buffer这个字节列表连接在一起，成为一个新的字节串

# 关闭连接:
s.close()



#接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
#第一次隔2行\r\n\r\n，1，区分头和内容
header,html = data.split(b'\r\n\r\n',1)
#header用utf-8解码
print(header.decode('utf-8'))
#二进位建立打开sina。html，html写入
with open('baidu.html','wb') as f:
    f.write(html)
