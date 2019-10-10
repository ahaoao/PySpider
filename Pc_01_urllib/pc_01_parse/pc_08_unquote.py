from urllib.parse import unquote

# unquote()可以对URL进行解码
url = "http://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8"
print(unquote(url))