from bs4 import BeautifulSoup
import requests


html = requests.get('http://www.badiu.com')
soup = BeautifulSoup(html.text, 'lxml')
print(soup.find_all(name='link'))
print(list(enumerate(soup.find_all(name='link'))))
print(type(soup.find_all(name='link')[0]))