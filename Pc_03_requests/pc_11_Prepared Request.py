from requests import Request, Session

URL = 'http://httpbin.org/post'
data = {
    'name': 'ahao'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/5'
                  '37.36 (KHTML, like Gecko) Chrome/74.0.3710.0 Safari/537.36'

}
s = Session()
req = Request('POST', URL, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)