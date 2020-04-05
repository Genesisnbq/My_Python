
# get  post 方式请求

# http://httpbin.org/   进行一些 http协议的测试

from urllib import request  # 处理请求
from urllib import parse  # 处理post数据
import urllib
import socket  # 套接字

data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')

print(data)

print('-'*40)

response = request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf8'))

print('-'*40)

response2 = request.urlopen(
    'http://httpbin.org/get', timeout=1)  # 如果超过1秒就会返回一个错误
print(response2.read())

print('-'*40)

# 可以使用try 来进行捕获
try:
    response3 = request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    # time out 的错误有很多种, 所以要加一个判断
    # 判断错误内容是否是超时
    if isinstance(e.reason, socket.timeout):
        print('Time Out')
