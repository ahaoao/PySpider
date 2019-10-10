import re


f = open('dianhua.txt', 'r')
html = f.read()
response = re.findall('\w{11}', html)
res = str(response)
with open('zhanghao.txt', 'a') as p:
    p.write(res+'\n')
h = open('zhanghao.txt', 'r')
html = re.findall('\w{11}', h.read())  # 匹配得到的是列表
for i in html:  # 遍历列表读取每个手机号
    with open('tiquzhanghao.txt', 'a') as f:
        f.write(i+'\n')