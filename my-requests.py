import requests

r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.text)
#对于带参数的URL，传入一个dict作为params参数：
r = requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
print(r.url)
#真实urlhttps://www.douban.com/search?q=python&cat=1001  查找python书籍，先去搜索 然后做出url模式

print(r.encoding)

print(r.content)
#requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
print(r.headers)
print(r.headers['Content-Type'])
#requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
r.cookies['ts']
print('#######')





#需要传入HTTP Header时，我们传入一个dict作为headers参数：
urlheader = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
r = requests.get('https://www.douban.com/', headers=urlheader)
print(r.text)

#要在请求中传入Cookie，只需准备一个dict传入cookies参数
cs = {'token':'12345','status':'working'}
r = requests.get(url.cookies)
#要指定超时，传入以秒为单位的timeout参数
r = requests.get(url,timeout=2.5)





#要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
urldata = {'form_email':'abc@example.com','form_password':'123456'}
r = requests.post('https://accounts.douban.com/login',data=urldata)

#如果要传递JSON数据，可以直接传入json参数：
params = {'key':'value'}
r = requests.post(url,json=params)## 内部自动序列化为JSON





#上传文件需要更复杂的编码格式，但是requests把它简化成files参数
#在读取文件时，注意务必使用'rb'即二进制模式读取，这样获取的bytes长度才是文件的长度。
upload_files = {'file':open('report.xls','rd')}
r = requests.post(url,files=upload_files)

