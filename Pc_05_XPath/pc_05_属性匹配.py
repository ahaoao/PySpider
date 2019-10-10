from lxml import etree


html = etree.parse('html.txt', etree.HTMLParser())
result = html.xpath('//div[@class="op-stockdynamic-moretab-map-tip"]')
# 可以用@符号进行过滤，比如这里选取class为op-stockdynamic-moretab-map-tip的节点
# 通过[@class="op-stockdynamic-moretab-map-tip"]限制了节点的class属性为op-stockdynamic-moretab-map-tip
# 如果调用了text方法表示筛选@,不过滤
print(result)