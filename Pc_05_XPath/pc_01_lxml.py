from lxml import etree


text = '''
<div class='masthead' style='margin-top:0px'>
<p class='text-warning'><a href='../Index.html'>返回主页</a>&nbsp;&nbsp;&nbsp;&nbsp;
<a href='userExit.aspx'>退出个人中心</a></p>                        
<ul class='nav nav-justified'>
'''
# etree模块可以自动修正HTML文本。
# tostring方法可以输出修正后的HTML代码，但是结果时bytes类型，这个用decode方法将其转化成str类型
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

# etree可以直接对文本进行解析，例如
html1 = etree.parse('html.txt', etree.HTMLParser())
result1 = etree.tostring(html1)
print(result1.decode('utf-8'))