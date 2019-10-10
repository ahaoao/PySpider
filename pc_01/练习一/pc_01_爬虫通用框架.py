import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "发生异常"


if __name__ == "__main__":
    url = "https://blog.csdn.net/qq_42022255/article/details/80687140"
    print(getHTMLText(url))