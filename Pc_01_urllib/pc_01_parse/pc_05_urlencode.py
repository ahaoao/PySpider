from urllib.parse import urlencode

# 调用urlencode方法将其序列化为GET请求参数
params = {
    'name': 'CSFR5XX',
    'age': '21'
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)