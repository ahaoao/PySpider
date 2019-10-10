from urllib.parse import quote

# quote()可以将内容转化为URL编码格式，URL中带有中文时，有时可能会导致乱码的问题，
# 调用这个方法可以将中文字符转化为URL编码
keyword = '壁纸'
url = 'http://www.baidu.com/s?wd=' + quote(keyword)
print(url)