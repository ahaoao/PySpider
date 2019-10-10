import requests
import re
import json


def get_one_page(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=169e85992fb48f-0cb571b68251da-4d045769-1fa400-169e85992fcc20;'
                  ' ASP.NET_SessionId=mif1t0ard5pvxun'
                  'kl4sdvom4; CNZZDATA5929667=cnzz_eid%3D1305202633-1554378632-%26ntime%3D1554603007',
        'Host': 'www.w23zu.cn:8000',
        'Referer': 'http://www.w23zu.cn:8000/userManage/Money.aspx',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ('
                      'KHTML, like Gecko) Chrome/58.0.3029.110 '
                  'Safari/537.36 SE 2.X MetaSr 1.0'
        }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def main():
    for i in range(4):
        url = 'http://www.w23zu.cn:8000/userManage/Message.aspx?selectPhone=&selectBTime=2019-04-07&page=' + str(i)
        html = get_one_page(url)
        result = re.findall('<td>\w{11}', html)
        with open('tel.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(result, ensure_ascii=False) + '\n')



main()
