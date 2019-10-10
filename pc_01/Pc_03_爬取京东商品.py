import requests
url = "https://www.amazon.cn/gp/product/B01HNYUG40/ref=s9_acsd_al_bw_c_x_3_w?pf_rd_m=A1U5RCOVU0NYF2&pf_rd_s=merchandised-search-3&pf_rd_r=Z3AH1HSZ2150HN03CHC6&pf_rd_t=101&pf_rd_p=effdfd06-48fd-4168-a492-e4b48173514d&pf_rd_i=1546136071"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")