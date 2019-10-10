from urllib.parse import urlsplit

# urlsplit 和 urlparse()方法类似，实现URL的分段和识别，只不过它不在单独解释 params（查询条件）这一部分
# 运行结果 SplitResult 是元组类型
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)
