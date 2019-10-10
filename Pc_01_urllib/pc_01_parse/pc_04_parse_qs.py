from urllib import request
from urllib import parse

# parse_qs 函数可以将经过编码后的url参数进行解码,即反序列化
params = {"name": "张三", "age": 18, "greet": "hello world"}
qs = parse.urlencode(params)
print(qs)
result = parse.parse_qs(qs)
print(result)
