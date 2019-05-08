#服务器会打开固定端口（比如80）监听，每来一个客户端连接，就创建该Socket连接
#服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理
import socket, threading, time

#实例化对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定监听地址和端口127.0.0.1是一个特殊的IP地址，表示本机地址
# 0.0.0.0绑定到所有的网络地址
s.bind(('127.0.0.1',9999))
#开始监听，参数等待连接的最大数量
s.listen(5)
print('Waiting for connection...')

#服务器程序通过一个永久循环来接受来自客户端的连接，
# accept()会等待并返回一个客户端的连接:
#每个连接都必须创建新线程（或进程）来处理

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        #当data空或是exit，跳出循环，否则hello加解码的数据，再编码
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))

    sock.close()
    print('Connection from %s:%s closed.' % addr)


#tcplink函数定义要放前面
while True:
    # 接受一个新连接: sock是连接的名字，addr 包含地址和端口
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

