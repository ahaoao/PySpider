from urllib.parse import urlencode
from pyquery import PyQuery as pq
import pymongo
import requests

# 连接数据库
Client = pymongo.MongoClient(host='localhost', port=27017)
db = Client['weibo']
collection = db['weibo']

base_url = 'https://m.weibo.cn/api/container/getIndex?'

# 请求头
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/5531524577',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '1858002662',
        'containerid': '1076031858002662',
        # 'since_id': '4305674366269334'
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['comments'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo


def save_to_mongo(result):
    if collection.insert(result):
        print('Saved to Mongo')


if __name__ == '__main__':
    for page in range(1, 20):
        json = get_page(page)
        results = parse_page(json)
        for result in results:
            save_to_mongo(result)
