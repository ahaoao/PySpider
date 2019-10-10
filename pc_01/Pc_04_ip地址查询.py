import requests
url = "http://www.ip38.com/ip.php?ip="
try:
    r = requests.get(url + '119.0.124.84')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")