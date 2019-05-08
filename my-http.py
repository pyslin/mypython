#HTML是一种用来定义网页的文本，会HTML，就可以编写网页；

#HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信。
#POST /path HTTP/1.1
#Header1: Value1
#Header2: Value2
#Header3: Value3
#当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。
#Body的数据类型由Content-Type头来确定，Content-Type: text/html,Body就是文本，如果是图片，Body就是图片的二进制数据。
#当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip