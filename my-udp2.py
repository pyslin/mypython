import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    print('send data: \r\n%s'%data.decode('utf-8'))
    s.sendto(data, ('127.0.0.1', 9999))

    # 接收数据:从服务器接收数据仍然调用recv()方法。
    print('receive data:')
    print(s.recv(1024).decode('utf-8'))
s.close()