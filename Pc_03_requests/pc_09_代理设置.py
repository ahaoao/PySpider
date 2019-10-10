import requests


# HTTP 协议代理
# proxies = {
#     'http:': 'http://115.203.97.26:9999',
#     'http:': 'http://122.193.247.82:9999'
# }
# r = requests.get('http://www.taobao.com', proxies=proxies)
# print(r.text)

# SOCKS协议代理
proxies = {
    'http:': 'socks5://115.203.97.26:9999',
    'http:': 'socks5://18985242014:MuXu2014@122.193.247.82:9999'
}
r = requests.get("http://www.taobao.com", proxies=proxies)
print(r.text)