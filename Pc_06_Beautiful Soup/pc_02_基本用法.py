from bs4 import BeautifulSoup
import requests

url = 'http://www.baidu.com/'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')

# 调用prettify()方法，这个方法可以 把解析的字符串以标准的缩进格式输出
# 对于不标准的HTML字符串BeautifulSoup可以自动更正格式。这一步不是由prettify做的，而是由BeautifulSoup初始化时完成的
print(soup.prettify())
print(soup.script.string)
# soup.script.string 输出HTML中的script节点的文本内容 