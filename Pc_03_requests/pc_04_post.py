import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                  '537.36 (KHTML, like Gecko) Chrome/74.0.3710.0 Safari/537.36'
}
data = {
    'name': 'CFSR5XX',
    'age': '21'
}
r = requests.post('http://www.httpbin.org/post', headers=headers, data=data)
print(r.text)