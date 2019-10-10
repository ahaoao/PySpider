import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) App'
                        'leWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36',
          }
html = requests.get(url, headers=header).text
doc = pq(html)
items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()

    # # open的第一个参数为保存的目标文件名称，第二个参数为a，代表追加方式写到文本，第三个指定文件的编码格式
    # file = open('.explore.txt', 'a', encoding='utf-8')
    # file.write('\n'.join([question, author, answer]))
    # file.write('\n' + '=' * 50 + '\n')
    # file.close()

    # 文件写入的简化形式with as 此方法结束时可以不用close()
    with open('.explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '=' * 50 + '\n')