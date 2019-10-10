from lxml import etree

# 这里的span节点的class属性有两个值fr和right，此时需要调用contains()方法
# contains方法第一个参数传入属性名称，第二个传入属性值。
html = etree.parse('html.txt', etree.HTMLParser())
result = html.xpath('//span[contains(@class, "right")]/a/text()')
# result = html.xpath('//span[@class="right"]/a/text()')
print(result)