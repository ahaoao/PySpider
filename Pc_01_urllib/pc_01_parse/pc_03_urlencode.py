from urllib import request
from urllib import parse

# urlencode 函数可以将url参数进行编码, 将参数字典转换为字符串
# params = {"name": "张三", "age": 19, "greet": "hello world"}
# result = params.urlencode(params)
# print(result)
url = "http://www.baidu.com/s"
params = {"wd": "刘德华"}
qs = parse.urlencode(params)
url = url + "?" + qs
resp = request.urlopen(url)
print(resp.read().decode())
