# -*- coding: utf-8 -*-
# @File   :wss_jrjr.py
# @Time   :2025/11/10 17:57
# @Author :admin

import execjs

def decrypt(data):
    with open('decrypt_jrjr.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    return execjs.compile(js_code).call('decrypt_', data)

def main():
    import requests

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.jrjr.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.jrjr.com/',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-storage-access': 'active',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    }

    params = {
        'a': 'dbkxian',
        'c': 'index',
        'v': 'v1',
        'key': '4f94ab4a71423706e537dcfe81565865',
        'access_token': '',
        'device': 'pc',
        'cv': '74',
        'appversion': '1.0.1',
        'lan': 'chinese',
        'u': '6',
        'tradeuser': '1118',
        'p_origin': 'jrjr',
    }

    json_data = {
        'symbol': 'GOLD',
        'periodType': 43200,
        'start': 0,
        'end': 1762822875,
    }

    response = requests.post(
        'https://alb-1ko0lowmvacsqia0ij.cn-shenzhen.alb.aliyuncsslb.com:39000/jrjr.php',
        params=params,
        headers=headers,
        json=json_data,
    )

    data = decrypt(response.json()['data'])
    print(data)

    return  data


if __name__ == '__main__':
    main()
