#encoding: utf-8


import urllib.request
import urllib.parse
import socket
import urllib.error


# urllib.request.urlopen(url, data=None, timeout=30, cafile=None, capath=None, cadefault=False, context=None)


# data参数是可选的，如果要添加该参数，需要使用bytes()方法将 参数 转化为 字节流编码格式的内容 即bytes类型，传递这个参数后为POST
data = bytes(urllib.parse.urlencode({"word": "hello"}), encoding="utf-8")
# urllib.parse模块里的urlencode()将参数字典转化为字符串
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))


# timeout 参数用于设置超时时间，单位为秒，如果请求超出这个时间，还没有得到响应，就会抛出异常
response = urllib.request.urlopen("http://httpbin.org/get", timeout=1)
print(response.read().decode("utf-8"))


# try except 语句抛出异常
try:
    response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")