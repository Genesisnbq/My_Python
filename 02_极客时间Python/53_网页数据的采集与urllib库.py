from urllib import request

url = "http://www.acwing.com"  # 告诉模块, 使用的是http协议

# 解析url

response = request.urlopen(url, timeout=1)  # 超过1秒, 网页没有打开, 就放弃打开这个网页

# 打开这个网页就像打开文件一样

print(response.read().decode('utf-8'))  # html的源代码

# utf-8
# GBK
# 网页源代码  html语法的相关解析
