#encoding: utf-8

from urllib import parse

# urlstring 这是必填项，待解析的url
# scheme:它是默认的协议，假如这个链接没有带协议信息，将会这个作为默认的协议。
url = "http://www.badiu.com/s?wd=python&username=abc#1"
# "urlparse"和"urlsplit"基本是一模一样，唯一不一样的地方是
# urlparse里面多了一个parse这个属性，而urlsplit没有
result1 = parse.urlparse(url)
result2 = parse.urlsplit(url)
print("scheme", result1.scheme)
print("netloc", result1.netloc)
print("path", result1.ptath)
print("params", result1.params)
print("query", result1.query)
print("fragment", result1.fragment)


