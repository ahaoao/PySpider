from lxml import etree
import pyquery

# @href 表示获取属性， 而 [@href="/jscode2011.htm"] 用来限定 /jscode2011.htm
html = etree.parse('html.txt', etree.HTMLParser())
# result = html.xpath('//tbody//*/@rrpyhohg')
result = html.xpath('//td//@rrpyhohg')
print(result)