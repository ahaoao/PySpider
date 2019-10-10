import requests


def getHTMLText(url, headers):
    s = requests.Session()
    s.get(url, headers=headers)
    r = s.get(url)
    r.encoding = r.apparent_encoding
    print(r.text)


if __name__ == "__main__":
    url = 'https://www.zhihu.com'
    headers = {
        'cookie': '_xsrf=n8HlqG7wmefkUABkiJ6ZkhJAdkyv50nk; _zap=12e98295-6812-4d10-aab5-0f941bf7991c; d_c0'
                  '="AJAjptau2g6PTvcKAymH16TOdEpofgTY_pI=|1547973733"; tgw_l7_route=060f637cd101836814f6c533'
                  '16f73463; capsion_ticket="2|1:0|10:1552316048|14:capsion_ticket|44:NDU5ZjZjZjU2Y2U4NDcyN2I'
                  'wZjkyMjVhM2I5OTNjMzA=|929949d3e2931c60eb78871c6671057d8d3ba9fadff3ab563815005559611875"; z_c'
                  '0="2|1:0|10:1552316162|4:z_c0|92:Mi4xbG4yeERnQUFBQUFBa0NPbTFxN2FEaVlBQUFCZ0FsVk5Bc1Z6WFFERDR'
                  'CbUYxTmMyLUxpNzJSNG9OTnpHMFY2YjZ3|15716380bd2961c40cb80809d383514cbcfc9cb0cd2835cb1191e8bd290'
                  '1e2a4"; tst=r'
    }
    getHTMLText(url, headers)