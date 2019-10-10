import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)

# 调用items()方法将得到的cookies的类型由RequestCookieJar转变为 元组 组成的 列表 元组里面有Key和Value
# 遍历出cookie的名称和值，实现cookie的遍历和解析
text = r.cookies.items()
print(text)

for key, value in r.cookies.items():
    print(key + '=' + value)