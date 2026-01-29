# -*- coding: utf-8 -*-
# @File   :xueqiu_login.py
# @Time   :2024/12/23 12:38
# @Author :admin

import subprocess
from functools import partial
from idlelib.iomenu import encoding

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

import time
import requests

def get_sign(params):
    with open('codejs_xueqiu_get_md5__1038.js', 'r', encoding='utf-8') as f:
        jscode = f.read()
    return execjs.compile(jscode).call('get_md5__1038', params)

def xueqiu_login():


    cookies = {
        'xq_a_token': 'cccb558956c11f5aaf8b9a30bcf1f214117e8d67',
        'xqat': 'cccb558956c11f5aaf8b9a30bcf1f214117e8d67',
        'xq_r_token': '4e5ca4e31de699c97d46d00138f4460861fd1778',
        'xq_id_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTczNjk4ODkwMCwiY3RtIjoxNzM0NzY1Njg0OTA1LCJjaWQiOiJkOWQwbjRBWnVwIn0.WlV2raM6_LItgNP1EGZSdZB6H6HKZqX49XAmfa7XMTimQxiggvRMDB4BIOEoJevlipQAOEEQTUqPjW9P_fsVhzNBPBnfD9ScSzQa9e-dUjVda4cqSVvY4wyTpwtp_6AZuhdA2ayvGTveclllUMyQ50kZtAtmWkK109zBDP4CY_tLJXYbna5hc_hN9LxK2VkQfETTzfMGoLxL0HqAJtZk_zpiLkJMK-pr_Gp9oQElBJvf-StLRswCz-55zGYvnqvghjJcuF7KKy2eHz68m6Og32ZQgfN2LjsQUeWg7eR3_dJ3koorMPuP1sN-HixTpat0P7w9ZaMx0qsmwuSv_vsfWw',
        'cookiesu': '661734765742142',
        'u': '661734765742142',
        'device_id': '94df5260a947926871572e9ebb63568c',
        'Hm_lvt_1db88642e346389874251b5a1eded6e3': '1734745111',
        '.thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7': '',
        'Hm_lpvt_1db88642e346389874251b5a1eded6e3': '1734922674',
        'ssxmod_itna': 'QuiQiKDKYv4jOx0xBcxBbRzIP0=qD8FttCSYNKB3WdDBLDAIoDZDiqAPGhDC845WmeabCYF+72C1jcAe0bYeIqiqC=fqjYdEnO4GLDmKDyKjh4GGBxBYDQxAYDGDDPzDj4ibDY4N8Djey1McHCLxiOD7eDXxGCDQIhP4DaDGaC1CWCbKK1oDDzoe84jYeDEevzh2Aht4D1qAHxPe5D9x0CDlaQBIiCDDHUMIDGSxLjpSR83fYDvxDkr+y7t8x14R58pFxYUCDYTQnxWAedPe24Gm0DWahosD+5Y02rIv05K0xBSvDDiPhqC7YziDD===',
        'ssxmod_itna2': 'QuiQiKDKYv4jOx0xBcxBbRzIP0=qD8FttCSYNKB3KD8LPeAI7D/+bSDF2oKQHUKGF3iQHxi59chF0m==Ko46egK8eP=i/8KoHY819Kk2X4n30A8v4g+pBjwUxMAd9x8wLS2MMqSztGqOOnNdchCmia5ZrcCWxRDQgexzPOitA5kqYnDacomQoIHI1Oa20yWf1pGvFSH6+gH1KmNkbujcFqkN60k1tibGbFzsa8x1EPT7KCGvpEt=TPkL2nsjx4E5jMvm/Gvz6DT5HaUQ=kbmetkWEGW/AO=/lB1PC3aRfuwrzGlzx4zgG3iGK7Sz4O1aRbh0dzrYEYG/dWiCxVu3j2qXOYdMWYrbSDk6OoFQ55YK4+33b3wCDXr86gtXuYo0ebb8cbpdCDidbWhQ9Sr=lFQeebhwgAxtT8tiiuSTdpo03+nbNRj+MS+oAw=OHcf+u+=5Y4eBQkEd=qxaoFVTxSgz4+sSr6ej3pQ5rBEbkxCls=3oKYaTpp41tzhzsq7EbEc7TRWToY4RGPbQYDLbn0oca0kOCrdTzgm660DIwoAD6DDwrWm+ILDowBIsehasr/cESo6bsKEaDoiR2h=c1rzyP6cPeYYFTe75Fn1jYaepuUYmmAAMLmGT=GzcKFGC8w10rpYjmmuNVU1F4gPjDXySuyueDGcDG7XoQ2GlNsEXx=yOxdr9Ydu7KUjmoQtq6hGYNnGKifzAKCGeiDD=',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain',
        # 'Cookie': 'xq_a_token=cccb558956c11f5aaf8b9a30bcf1f214117e8d67; xqat=cccb558956c11f5aaf8b9a30bcf1f214117e8d67; xq_r_token=4e5ca4e31de699c97d46d00138f4460861fd1778; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTczNjk4ODkwMCwiY3RtIjoxNzM0NzY1Njg0OTA1LCJjaWQiOiJkOWQwbjRBWnVwIn0.WlV2raM6_LItgNP1EGZSdZB6H6HKZqX49XAmfa7XMTimQxiggvRMDB4BIOEoJevlipQAOEEQTUqPjW9P_fsVhzNBPBnfD9ScSzQa9e-dUjVda4cqSVvY4wyTpwtp_6AZuhdA2ayvGTveclllUMyQ50kZtAtmWkK109zBDP4CY_tLJXYbna5hc_hN9LxK2VkQfETTzfMGoLxL0HqAJtZk_zpiLkJMK-pr_Gp9oQElBJvf-StLRswCz-55zGYvnqvghjJcuF7KKy2eHz68m6Og32ZQgfN2LjsQUeWg7eR3_dJ3koorMPuP1sN-HixTpat0P7w9ZaMx0qsmwuSv_vsfWw; cookiesu=661734765742142; u=661734765742142; device_id=94df5260a947926871572e9ebb63568c; Hm_lvt_1db88642e346389874251b5a1eded6e3=1734745111; .thumbcache_f24b8bbe5a5934237bbc0eda20c1b6e7=; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1734922674; ssxmod_itna=QuiQiKDKYv4jOx0xBcxBbRzIP0=qD8FttCSYNKB3WdDBLDAIoDZDiqAPGhDC845WmeabCYF+72C1jcAe0bYeIqiqC=fqjYdEnO4GLDmKDyKjh4GGBxBYDQxAYDGDDPzDj4ibDY4N8Djey1McHCLxiOD7eDXxGCDQIhP4DaDGaC1CWCbKK1oDDzoe84jYeDEevzh2Aht4D1qAHxPe5D9x0CDlaQBIiCDDHUMIDGSxLjpSR83fYDvxDkr+y7t8x14R58pFxYUCDYTQnxWAedPe24Gm0DWahosD+5Y02rIv05K0xBSvDDiPhqC7YziDD===; ssxmod_itna2=QuiQiKDKYv4jOx0xBcxBbRzIP0=qD8FttCSYNKB3KD8LPeAI7D/+bSDF2oKQHUKGF3iQHxi59chF0m==Ko46egK8eP=i/8KoHY819Kk2X4n30A8v4g+pBjwUxMAd9x8wLS2MMqSztGqOOnNdchCmia5ZrcCWxRDQgexzPOitA5kqYnDacomQoIHI1Oa20yWf1pGvFSH6+gH1KmNkbujcFqkN60k1tibGbFzsa8x1EPT7KCGvpEt=TPkL2nsjx4E5jMvm/Gvz6DT5HaUQ=kbmetkWEGW/AO=/lB1PC3aRfuwrzGlzx4zgG3iGK7Sz4O1aRbh0dzrYEYG/dWiCxVu3j2qXOYdMWYrbSDk6OoFQ55YK4+33b3wCDXr86gtXuYo0ebb8cbpdCDidbWhQ9Sr=lFQeebhwgAxtT8tiiuSTdpo03+nbNRj+MS+oAw=OHcf+u+=5Y4eBQkEd=qxaoFVTxSgz4+sSr6ej3pQ5rBEbkxCls=3oKYaTpp41tzhzsq7EbEc7TRWToY4RGPbQYDLbn0oca0kOCrdTzgm660DIwoAD6DDwrWm+ILDowBIsehasr/cESo6bsKEaDoiR2h=c1rzyP6cPeYYFTe75Fn1jYaepuUYmmAAMLmGT=GzcKFGC8w10rpYjmmuNVU1F4gPjDXySuyueDGcDG7XoQ2GlNsEXx=yOxdr9Ydu7KUjmoQtq6hGYNnGKifzAKCGeiDD=',
        'Origin': 'https://xueqiu.com',
        'Pragma': 'no-cache',
        'Referer': 'https://xueqiu.com/?md5__1038=QqGxcDnDyiitnD05o4%2Br%3DFYG%3Dqw4u0bD',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'elastic-apm-traceparent': '00-dacfd46e74487a6a49734e2c1b47dcf1-b9724165effef4a4-01',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'category': 'web_behavior',
        # 'md5__1038': 'n40h0KGK4IxGxeqx0vk4xy0bGCDRiB2YgCCoD',
    }

    time_stamp = int(time.time() * 1000)
    data = '-1|'+str(time_stamp)+'|windows|1920x1080|112|1000|1|{"cookiesu":"661734765742142","ua":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36","referurl":"https://xueqiu.com/?md5__1038=QqGxcDnDyiitnD05o4%2Br%3DFYG%3Dqw4u0bD","url":"https://xueqiu.com/?md5__1038=QqGxcDnDyiitnD05o4%2Br%3DFYG%3Dqw4u0bD","deviceid":"94df5260a947926871572e9ebb63568c","trigger":"undefined","source":500,"method":"password"}'
    data = f'https://xueqiu.com/upload/web?category=web_behavior{data}'

    sign = get_sign(data)
    print(sign)
    params['md5__1038'] = sign
    response = requests.post('https://xueqiu.com/upload/web', params=params, cookies=cookies, headers=headers,
                             data=data)
    print(response.json())

if __name__ == '__main__':
    xueqiu_login()
