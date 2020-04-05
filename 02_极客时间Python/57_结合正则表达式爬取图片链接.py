import requests
import re # 正则表达式库

content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
print(content) # 显示的内容比较混乱

# 提取图片的链接

print('-'*40)

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>',re.S)
results = re.findall(pattern,content)
print(results)

print('-'*40)

for result in results:
    url,name=result
    print(url,re.sub('\s','',name)) # '\s' 匹配空白的字符(把 \n,\p等制表符, 都能匹配上)
    
