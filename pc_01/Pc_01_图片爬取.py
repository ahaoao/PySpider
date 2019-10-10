import requests
import os
url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1550309551763&di=997b1248359203e04019a707b7cae14a&imgtype=0&src=http%3A%2F%2Fimages.enet.com.cn%2F2011%2F4%2F19%2F1304713401519.jpg"
root = "E://pics//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已经存在")
except:
    print("爬取失败")