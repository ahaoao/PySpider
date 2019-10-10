import requests


url = "https://tieba.baidu.com/index.html"
header = {
    'Cookie': '__cfduid=d225b5460dd3c0b7ec99d40bd8ff0fd351541774482; TIEBAUID=d628139fffe8742d3cdb679d; '
              'TIEBA_USERTYPE=b202ce22ea5e36a327f7e64a; bdshare_firstime=1542281315305; rpln_guide=1; BAI'
              'DUID=DDB376D37D3B99523F498F8DD1CCFF17:FG=1; PSTM=1556283007; BIDUPSID=53BAFBF84FC88970C2C3'
              'DB6F59041BB7; BDUSS=TdLcVVoVnJESkV2bm5yNjc5MHA3ZU5qckxqWmJSNn43Ti1Za0dhVWtPS0FlMGxkSVFBQUF'
              'BJCQAAAAAAAAAAAEAAABNCYNiSGFvMTEzMTExMjY1MgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
              'AAAAAAAAAAAAAAAAAAIDuIV2A7iFdZ; STOKEN=f733e96fb05602526326b7bfa29c6a49f319993a25d3df557c2a71'
              '41744e4b24; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; H_PS_PSSID=1996_1468_21080'
              '_18560_29522_29520_29099_29634_29568_29220_26350_28703; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598'
              '; td_cookie=2672322361; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1565937349,1565950173,1566139885'
              ',1566358405; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1566358405',
    'Host': 'tieba.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.'
                  '110 Safari/537.36 SE 2.X MetaSr 1.0'
}

html = requests.get(url, headers=header)
print(html.text)