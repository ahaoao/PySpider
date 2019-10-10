from lxml import etree
blockid="lianmeng_mask"
#
html = etree.parse('html.txt', etree.HTMLParser())
result = html.xpath('//span[contains(@class, "f1") and @name="m1"]//text()')
print(result)