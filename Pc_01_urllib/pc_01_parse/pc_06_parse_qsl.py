from urllib.parse import parse_qsl

# parse_qsl()将参数转化为元组组成的列表，元组的第一个元素时参数名，第二个内容是参数值
query = 'name=germey&age=22'
print(parse_qsl(query))