from urllib.parse import urlparse

result = urlparse('http://baidu.com/index.html;user?id=5#comment')
print(type(result), result)

# urlstring 这是必填项，待解析的url
# scheme:它是默认的协议，假如这个链接没有带协议信息，将会这个作为默认的协议。