import requests
import re
from requests.exceptions import RequestException
import json
import base64


def get_wechat_page(url):
    try:
        wechat = requests.get(url)
        if wechat.status_code == 200:
            return wechat.text
        return None
    except RequestException:
        return None


def parse_wechat_page(html):
    pattern = re.compile('[a-zA-z]+://[^\s]*', re.S)
    items = re.findall(pattern, html)
    return items
    # for item in items:
    #     yield{
    #         'index': item[0:]
    #     }


def write_to_file_info(content):
    with open('wechat1.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        f.close()


def write_to_file_photo(po):
    i = 1
    for url2 in po:
        jpeg = requests.get(url2)
        with open('wechat1' + str(i) + '.jpeg', 'rb') as h:
            h.write(jpeg.content)
            h.close()
        i = i + 1


def main():
    url = 'https://mp.weixin.qq.com/s/1IO8KgQBIgW-qdfy6pHDgA'
    html = get_wechat_page(url)
    write_to_file_info(html)
    write_to_file_photo(html)


if __name__ == '__main__':
    main()

