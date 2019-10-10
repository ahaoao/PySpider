from bs4 import BeautifulSoup
import requests


# 直接调用节点的名称就可以选择节点元素，再调用string属性就可以得到节点内的文本了。这种选择速度非常快。
# 1.选择元素
url = 'http://www.baidu.com/'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'lxml')
print(soup.script)
print(type(soup.script))
print(soup.script.string)
print(soup.head)
print(soup.p)
# 当有多个相同的节点时，这种选择方式只会选择到第一个匹配的节点，其他后面的节点会被忽略

# 2.提取信息
# （1）获取名称  : 可以利用name属性获取节点的名称。
print(soup.script.name)

# （2）获取属性  ：每个节点可能有多个属性，比如id和class等，选择这个节点元素后，可以调用attrs获取所有属性
print(soup.img.attrs)
print(soup.img.attrs['height'])

# （3）.获取内容：利用string属性就可以
print(soup.script.string)