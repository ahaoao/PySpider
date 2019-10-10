import requests


def get_page(url):
    headers = {
        'Host': 'wq.jd.com',
        'Connection': 'keep - alive',
        'Cache - Control': 'max - age = 0',
    'Upgrade - Insecure - Requests': '1',
    'User - Agent': 'Mozilla / 5.0(Windows'
    'NT'
    '10.0;'
    'WOW64) AppleWebKit / 537.36(KHTML, like'
    'Gecko) Chrome / 58.0'
    '.3029'
    '.110Safari / 537.36SE2.XMetaSr1.0',
    'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
    'Accept - Encoding': 'gzip, deflate, sdch, br',
    'Accept - Language': 'zh - CN, zh;q = 0.8',
    'cookie': 'shshshfpa=9c17ebfc-b619-cf4c-9330-517f728b6a64-1541771953; TrackID=1xSp8oQEwsh875C2ekDINuCagv5rXR_m'
              'jthtkufBS3roNlNU1GgzKDC_6TA6fqxwhd460Hyt2juhcWxOoC_C8MpJh9UvtOq3rG0VOLYSp_O4; pinId=GRGvtiTpxORtIUJ7F'
              'wjQr7V9-x-f3wj7; __jdv=122270672|cuiqingcai.com|-|referral|-|1554881817021; ipLoc-djd=1-72-2799-0; ip'
              'Location=%u5317%u4EAC; areaId=1; PCSYCityID=22; __jdu=1037148160; webp=1; sc_width=1920; visitkey=1119'
              '2600360820551; __jda=122270672.1037148160.1541769605.1555122464.1555124412.13; 3AB9D23F7A4B3C9B=4CPPG7'
              'SAW44TCT7BZDDVWBZD5GFCB6XKUCMVH6FRBIUIDLDERYXQP3KHXWK6CRKFSDZUP4LLVZLX4E6KTQDCDF3JD4; TrackerID=6LolFxB'
              '0gexvP2xBiN3C-sPvP-C-dFso3QTkAkHyiCFpDEBRQWfxo-JpgyUqv_cocG4BbDlduUewtpGVe2uQzvLhwh0wxlav4NkA8dPi6N0; pt'
              '_key=AAJcsVDQADABv8E6j9ykW4p2YiIS91q6HS-lo5mlOzkMnhov4DKJAFOT11xt_CXUvCGhgVC2PhE; pt_pin=jd_drXwJlXJsMSB'
              '; pt_token=cm64eu8k; pwdt_id=jd_drXwJlXJsMSB; mba_muid=1037148160; buy_uin=21752595859; jdpin=jd_drXwJlXJs'
              'MSB; pin=jd_drXwJlXJsMSB; wq_skey=zm2E09E990992A9FC01087C59C934E6C30D43A942C4860357D3F07832068E9966980A31B4'
              'BF4E82F09C8EC66B6345960BF53822FC87ECE69858109921EE27E23C4DD4D57ABB686CEAC1CE34CF1E8A74740; wq_uin=2175259585'
              '9; wxa_level=1; retina=0; cid=3; __wga=1555132742717.1555132742717.1555127515428.1555119422589.1.4; PPRD_P=UUI'
              'D.1037148160; wq_area=22_1930_0%7C2; shshshfp=bf4bf4fc7f278c7535d8b8c85120c969; shshshsID=834297a36d4116011e2115'
              '655eb266ef_1_1555132743591; shshshfpb=19c5ff20bf7c9421186bf8311900b84a882f525ef071bb56c5be592b2c; promotejs=2f563'
              '14761c37d2786735ff2a10ade4017CIT'

    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text


def main():
    url = 'https://wq.jd.com/cube/front/activePublish/rrbv3/143203.html?' \
          '_wv=1&activenologin=1&_mlogin=1&suin=21752595859&md5=d41f8ed5f829eb878cf40724b9e2b3d6'
    html = get_page(url)
    print(html)


if __name__ == '__main__':
    main()
