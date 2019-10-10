from urllib.parse import urljoin

# urljoin 可以提供一个base_url 作为一个参数，将新的链接作为第二个参数，该方法会分析base_url的scheme, netloc,和path
# 这三个内容并对新链接缺失的部分进行补充，最后返回结果
# base_url 提供了三项内容 scheme，netloc，path，如果这三项在新的链接里不存在，就予以补充，如果新链接存在，就使用新链接的部分
# base_url中的params，query，和fragment，是不起作用的
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.badiu.com', 'http://cuiqingcai.com'))
print(urljoin('http://www.baidu.com/about.html', 'http://cuiqingcai.com'))
print(urljoin('http://www.baidu.com#comment', '?category=2'))
