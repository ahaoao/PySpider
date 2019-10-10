from lxml import etree

# //* 代表匹配所有节点   //节点名称   例如 //li 表示选取所有li节点
html = etree.parse('html.txt', etree.HTMLParser())
result = html.xpath('//div')
print(result)
print(result[0])
