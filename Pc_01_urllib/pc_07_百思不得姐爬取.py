from urllib import parse,request


url = "http://www.budejie.com/2"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) Ap"
                  "pleWebKit/537.36 (KHTML, like Gecko) Ch"
                  "rome/58.0.3029.110 Safari/537.36 SE 2.X"
                  " MetaSr 1.0"
}

req = request.Request(url, headers=headers)
resp = request.urlopen(req)
print(resp.read())
# resp = request.urlopen(url)
# print(resp.read())