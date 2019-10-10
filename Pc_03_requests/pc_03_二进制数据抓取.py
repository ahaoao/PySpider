import requests

# Response对象的两个属性，一个是text，一个是content
r = requests.get('http://i1.mopimg.cn/img/tt/2017-06/779/20170624084853601.JPEG')
# print(r.text)
# print(r.content)


# 对抓取到的图片进行保存
with open('mn12.png', 'wb') as f:
    f.write(r.content)

# 这里调用了open()方法，它的第一个参数是文件名称，第二个参数代表以二进制写的形式打开，可以向二进制文件里写入二进制数据

