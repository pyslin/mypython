
import random
import urllib.request

url = 'https://www.baidu.com/s'

# 采用随机的user-agent
headers = [
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
]
user_agent = random.choice(headers)

# 对输入的关键字进行url编码
wd = input('请输入想要搜索的关键字：')
wd = urllib.request.quote(wd)

full_url = url+'?wd='+wd

# 创建请求对象
request = urllib.request.Request(full_url)

# 添加请求头信息
request.add_header('User-Agent', user_agent)

# 打印请求头信息，查看是否正确
print(request.get_full_url())

# 获取返回信息
response = urllib.request.urlopen(request)
html = response.read()
print(html.decode('utf-8'))