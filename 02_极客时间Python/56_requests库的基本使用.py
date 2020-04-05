import requests

# get请求
url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc':'xyz'}

response = requests.get(url,data)

print(response.text)

print('-'*40)

# post请求
url = 'http://httpbin.org/post'
data = {'key': 'value', 'abc':'xyz'}

response = requests.post(url,data)

print(response.text)

print('-'*40)

print(response.json)