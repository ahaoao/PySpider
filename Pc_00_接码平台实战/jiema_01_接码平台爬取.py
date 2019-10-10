import requests
import re
import json


def get_one_page(url):
        """

        :param url: 抓取网页地址
        :return: 抓取的网页源代码
        """

        # 构造消息头，模拟网页登录
        headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'UM_distinctid=169f7da1cd242-03459374723607-70113f4b-144000-169f7da1cd33; CNZZD'
                  'ATA5929667=cnzz_eid%3D1541571193-1554638426-%26ntime%3D1554805243; ASP.NET_Sessi'
                  'onId=jykztc2n1qxfksbnavpguhud',
        'Host': 'www.w23zu.cn:8000',
        'Referer': 'http://www.w23zu.cn:8000/userManage/Money.aspx',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like '
                      'Gecko) Chrome/58.0.3029.110 '
                  'Safari/537.36 SE 2.X MetaSr 1.0'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text


# 正则匹配抓取的网页手机号码
def parse_one_page(html):
    pattern = re.compile('<td>(\w{11})</td>', re.S)
    items = re.findall(pattern, html)
    return list(items)
    # for item in items:
    #     yield{
    #         items[0:]
    #     }


# 匹配的手机号保存在本地文件
def write_to_file(content):
    with open('T.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(i):
    url = 'http://www.w23zu.cn:8000/userManage/Message.aspx?selectPhone=&selectBTime=2019-04-07&page=' + str(i)  # 构造网页
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(252):  # 构造网页 1-252页
        main(i)