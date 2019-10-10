from urllib.request import HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, build_opener
from urllib.error import URLError

password = 'MuXu2014'
url = 'http://192.168.1.1'
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, user=None, passwd=None)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode("utf-8")
    print(html)
except URLError as e:
    print(e.reason)
