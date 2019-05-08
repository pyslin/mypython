#检测网页字符串编码
import chardet
#引入包

data1 = b'Hello'
print(chardet.detect(data1))

data2 ='离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data2))
