import requests
from requests.auth import HTTPBasicAuth

r = requests.get('http://192.168.1.1/', auth=(None, 'MuXu2014'))
print(r.text)
