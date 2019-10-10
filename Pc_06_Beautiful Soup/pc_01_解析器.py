from bs4 import BeautifulSoup

# 使用lxml解析器，初始化BeautifulSoup时可以把第二个参数修改成lxml
# 第一个参数就是传入的对象
soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)
# lxml解析器有解析HTML和XML的功能

# BeautifulSoup 支持的解析器
# python标准库        BeautifulSoup(markup, 'html.parser')
# lxml HTML 解析器    BeautifulSoup(markup, 'lxml')
# lxml XML 解析器     BeautifulSoup(markup, 'xml')
# html5lib            BeautifulSoup(markup, 'html5lib')
