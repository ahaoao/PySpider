import requests

def get_page(url):
    headers = {
    'User-Agent': 'mozilla/5.0 (linux; u; android 4.1.2; zh-cn; mi-one plus build/jzo54k'
                  ') applewebkit/534.30 (khtml, like gecko) version/4.0 mobile safari/534'
                  '.30 micromessenger/5.0.1.352'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def main():
    url = 'http://sendbookbeta.chuangdu.vip/gh_822ae6876340/mine/inviterecord?apply_id=294619'
    html = get_page(url)
    print(html)


if __name__ == '__main__':
    main()
