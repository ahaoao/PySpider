import requests

url = 'https://www-k6.thinkcentral.com/content/hsp/math/hspmath/na/gr4/ese_9780547879123_/launch.html'
r = requests.get(url)
r.encoding = r.raise_for_status()
print(r.text)