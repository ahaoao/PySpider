from lxml import etree

# 子节点 比如选择选择div节点的所有直接a子节点，//div/a   若选取div下的所有子孙a节点，则为 //div//a
html = etree.parse('html.txt', etree.HTMLParser())
result = html.xpath('//div/a')
print(result)