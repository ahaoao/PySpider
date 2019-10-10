from lxml import etree
# 如果想要获取span节点内部的文本，就有两种方式，一种是先选取a节点再获取文本，另外一种是使用//
# 如果想要获取某些特定子孙节点下的所有文本，可以选取到特定的子孙节点，然后调用text()方法
html = etree.parse('html.txt', etree.HTMLParser())
result = html.xpath('//span[@class="l"]//text()')
print(result)