#摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
# 而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。

import hashlib

md5 = hashlib.md5()
print(type(md5)) #一个md5类对象
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.digest())
print(md5.hexdigest()) # 使用一个 32 位的 16 进制字符串表示

import hashlib
sha1 = hashlib.sha1()
sha1.update('md5 test in Python!'.encode('utf-8'))
sha1.update('the salt'.encode('utf-8'))
print(sha1.hexdigest())

#hmac模块实现了标准的Hmac算法。我们来看看如何使用hmac实现带key的哈希
import hmac
#通常是str b是bytes
message = b'Hello,world!'
key = b'secret'


