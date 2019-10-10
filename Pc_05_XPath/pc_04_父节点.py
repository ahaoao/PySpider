from lxml import etree


html = etree.parse('html.txt', etree.HTMLParser())
result = html.xpath('//a[@href="link1.html"]/../@class')
print(result)