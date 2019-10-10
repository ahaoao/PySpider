from bs4 import BeautifulSoup
import requests


url = 'http://www.baidu.com/'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)