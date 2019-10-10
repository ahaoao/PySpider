import requests

# 添加headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/74.0.3710.0 Safari/537.36'
}
url = 'http://httpbin.org/post'
data = {
    "name": 'CFSSRXX',
    "age": 22
}
r = requests.get('http://httpbin.org/get', headers=headers, params=data)
print(r.text)