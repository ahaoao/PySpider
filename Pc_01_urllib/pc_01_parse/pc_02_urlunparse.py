# urlunparse它接收的参数是一个可迭代对象，参数个数必须为6个
# 该方法将各部分进行拼接，组成URL

from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

