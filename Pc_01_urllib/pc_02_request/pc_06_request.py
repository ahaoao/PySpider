#encoding: utf-8

from urllib import request
from urllib import parse

url = "http://htttpbin.org/post"

# 请求头
headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Host": "httpbin.org"
}

dict_1 = {
    "name": "Germey"
}
data = bytes(parse.urlencode(dict_1), encoding="utf8")

req = request.Request(url=url, data=data, headers=headers, method="POST")
response = request.urlopen(req)
print(response.read().decode("utf-8"))


