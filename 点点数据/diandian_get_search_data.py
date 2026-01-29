# -*- coding: utf-8 -*-
# @File   :diandian_get_search_data.py
# @Time   :2024/12/31 13:07
# @Author :admin

import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

def get_sign(params):
    with open('codejs_diandian_get_sign.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    return execjs.compile(js_code).call('get_sign', params)

def get_search_data(keyword="", page=1, page_size=10):
    import requests

    cookies = {
        'deviceid': '8ca90261fcec571f2e46a0de4223bf5',
        'Hm_lvt_4b46d92b8c2be1622e347873de8ada00': '1735540894',
        'HMACCOUNT': 'B050A7F72F744AE6',
        'Hm_lvt_c420cc498e4250baa6114afe2947045e': '1735540894',
        'Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f': '1735540894',
        '_ga': 'GA1.1.1846972073.1735540897',
        'Qs_lvt_404253': '1735616116',
        'Qs_pv_404253': '507178610993153900',
        'Hm_lpvt_4b46d92b8c2be1622e347873de8ada00': '1735618517',
        'Hm_lpvt_c420cc498e4250baa6114afe2947045e': '1735618517',
        'Hm_lpvt_e1382854e68f4d69f837bb54a6d1e22f': '1735618517',
        '_uetsid': '1d7a5c00c67911ef95773100d91bf041',
        '_uetvid': '1d7a8330c67911ef83bc415b4d9fb910',
        '_ga_GVCWL6PNZ2': 'GS1.1.1735621590.6.0.1735621590.0.0.0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'deviceid=8ca90261fcec571f2e46a0de4223bf5; Hm_lvt_4b46d92b8c2be1622e347873de8ada00=1735540894; HMACCOUNT=B050A7F72F744AE6; Hm_lvt_c420cc498e4250baa6114afe2947045e=1735540894; Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f=1735540894; _ga=GA1.1.1846972073.1735540897; Qs_lvt_404253=1735616116; Qs_pv_404253=507178610993153900; Hm_lpvt_4b46d92b8c2be1622e347873de8ada00=1735618517; Hm_lpvt_c420cc498e4250baa6114afe2947045e=1735618517; Hm_lpvt_e1382854e68f4d69f837bb54a6d1e22f=1735618517; _uetsid=1d7a5c00c67911ef95773100d91bf041; _uetvid=1d7a8330c67911ef83bc415b4d9fb910; _ga_GVCWL6PNZ2=GS1.1.1735621590.6.0.1735621590.0.0.0',
        'Origin': 'https://www.diandian.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.diandian.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'business': '1',
        'genre_id': '',
        'sub_genre': '',
        'word': f'{keyword}',
        'page': f'{page}',
        'pagesize': f'{page_size}',
    }

    k = get_sign(params)
    params['k'] = k
    print(k)
    print(params)

    response = requests.get('https://api.diandian.com/pc/app/v1/info/search', params=params, cookies=cookies,
                            headers=headers)
    print(response.url)
    print(response.json())


def get_data():
    import requests

    cookies = {
        'deviceid': '8ca90261fcec571f2e46a0de4223bf5',
        'Hm_lvt_4b46d92b8c2be1622e347873de8ada00': '1735540894',
        'HMACCOUNT': 'B050A7F72F744AE6',
        'Hm_lvt_c420cc498e4250baa6114afe2947045e': '1735540894',
        'Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f': '1735540894',
        '_ga': 'GA1.1.1846972073.1735540897',
        'Qs_lvt_404253': '1735616116',
        'Qs_pv_404253': '507178610993153900',
        'Hm_lpvt_4b46d92b8c2be1622e347873de8ada00': '1735618517',
        'Hm_lpvt_c420cc498e4250baa6114afe2947045e': '1735618517',
        'Hm_lpvt_e1382854e68f4d69f837bb54a6d1e22f': '1735618517',
        '_uetsid': '1d7a5c00c67911ef95773100d91bf041',
        '_uetvid': '1d7a8330c67911ef83bc415b4d9fb910',
        '_ga_GVCWL6PNZ2': 'GS1.1.1735621590.6.1.1735622302.0.0.0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'deviceid=8ca90261fcec571f2e46a0de4223bf5; Hm_lvt_4b46d92b8c2be1622e347873de8ada00=1735540894; HMACCOUNT=B050A7F72F744AE6; Hm_lvt_c420cc498e4250baa6114afe2947045e=1735540894; Hm_lvt_e1382854e68f4d69f837bb54a6d1e22f=1735540894; _ga=GA1.1.1846972073.1735540897; Qs_lvt_404253=1735616116; Qs_pv_404253=507178610993153900; Hm_lpvt_4b46d92b8c2be1622e347873de8ada00=1735618517; Hm_lpvt_c420cc498e4250baa6114afe2947045e=1735618517; Hm_lpvt_e1382854e68f4d69f837bb54a6d1e22f=1735618517; _uetsid=1d7a5c00c67911ef95773100d91bf041; _uetvid=1d7a8330c67911ef83bc415b4d9fb910; _ga_GVCWL6PNZ2=GS1.1.1735621590.6.1.1735622302.0.0.0',
        'Origin': 'https://www.diandian.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.diandian.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'business': '2',
        'genre_id': '',
        'sub_genre': '',
        'word': '',
        'page': '2',
        'pagesize': '10',
        'k': 'BRFcBUJPA2lGRAMYWQNfXBVzX1ISCApTQk8DaVgCBQ4HWQwGCjMSFUZCBg==',
    }

    k = get_sign(params)
    params['k'] = k
    print(k)

    response = requests.get('https://api.diandian.com/pc/app/v1/info/search', params=params, cookies=cookies,
                            headers=headers)
    print(response.json())


if __name__ == '__main__':
    get_data()
