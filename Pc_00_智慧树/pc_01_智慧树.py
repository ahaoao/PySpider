import requests
import re

headers = {
    'cookie': 'RK = ywYcSyKtWe;ptcz = 72cf00d95350c8c80d06255402c51c6d2e4fd25a571bdadedb6688cf818ff406;'
              'pgv_info = ssid = s3075305618;pgv_pvid = 4707458736;pgv_pvi = 1590987776;pgv_si = s6022652928;'
              'uin = o1413767305;skey =@XsbaKTEop; ptisp = cnc;p_uin = o1413767305;pt4_token = xpuup - fkN4M3F'
              'qBgRS38DuVSvmRl3cduIebi * BoiobY_;p_skey = DIysIjnEQARGKDmhNCodPWXDh4VfrNhLI83oPM4HjEQ_;wimrefre'
              'shrun = 0 &;qm_logintype = qq;qm_flag = 0;qqmail_alias = 1413767305 @ qq.com;sid = 1413767305 & 08e23'
              'f260c134483668e55bca581b09f, qREl5c0lqbkVRQVJHS0RtaE5Db2RQV1hEaDRWZnJOaExJODNvUE00SGpFUV8.;qm_username = 1413767305;'
              'qm_domain = https: // mail.qq.com;qm_ptsk = 1413767305 &@XsbaKTEop; foxacc = 1413767305 & 0;ssl_edition'
              ' = sail.qq.com;edition = mail.qq.com;qm_loginfrom = 1413767305 & wpt;username = 1413767305 & 1413767305;new_mail_nu'
              'm = 1413767305 & 11;webp = 1;qm_sid = 08e23f260c134483668e55bca581b09f, qREl5c0lqbkVRQVJHS0RtaE5Db2RQV1h'
              'EaDRWZnJOaExJODNvUE00SGpFUV8.;_qpsvr_localtk = 0.6540149185206139;_qz_referrer = qzone.qq.com;CCSHOW = 000000q - guid'
              ': cb0ea7f123772a797faaf105377988cbq - ua2: PR = PC & CO = WBK & QV = 3 & PL = WIN & PB = GE & PPVN = 10.4.0'
              '.3457 & COVC = 047000 & CHID = 43653 & RL = 1920 * 1080 & MO = QB & VE = GA & BIT = 64 & OS = 10.0.17134'
              'upgrade - insecure - requests: 1',
'user - agent': 'Mozilla / 5.0(WindowsNT10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrom'
                'e / 70.0.3538.25Safari / 537.36'
}
url = 'https://user.qzone.qq.com/1413767305'
r = requests.get(url, headers=headers)
print(r.text)