# -*- coding: utf-8 -*-
# @File   :api_account_login.py
# @Time   :2026/1/30 13:30
# @Author :admin


import execjs

js_code = open('./shopee_login_jsCode.js', 'r', encoding='utf-8').read()
cxt = execjs.compile(js_code)


def api_account_login(username, password):
    import requests

    cookies = {
        '_QPWSDCXHZQA': '4769076e-9b5d-4918-b1d1-827ac3166dd6',
        'REC7iLP4Q': 'bf29af4b-6025-4cc8-b8ce-7534c84203f8',
        'SPC_SEC_SI': 'v1-ZFBzeFlKcVY3ZmdGYUhqYuG94qntLgMzchyCQfG+Ad3J6ljhXBHKznnOrTHiQGgpr3GQ5+sh8bE5Feqmxuozi2pljtkOAf1LUY/a/ZJTJGw=',
        'SPC_SI': '3ddyaQAAAABxNVVzN2lQej3lhgcAAAAAQUJiWGZtNjM=',
        'SPC_F': 'duvWxnwKIarmRhnYfZJQChOKFMsGgMxJ',
        'SC_DFP': 'WbAhlyqTunwSAUugbfThXjWcmiWtHjFl',
        'osid.f9ffc83459897a13dd14c537e84b1753': '1b88a83f67a005f02ed4c046de9587cd',
        'shopee_webUnique_ccd': 'ivLtK4ve47txnhWdxvQgZg%3D%3D%7CcWjWZ0aI3YAhauaJcpg74VimNMnkUj6203MWmHMjRW6sPju6mv%2FiKX7mYOoCD2SVODKwu%2BYV1ben5lU%3D%7CckYNjw3OuKPo6dnY%7C08%7C3',
        'ds': 'ca76e8f5a7ff76bee5d5d803ef005a82',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'af-ac-enc-sz-token': 'FULz/pwmpiS3uPlh3VDA7Q==|cWjWZ0aI3YAhauaJcpg74VimNMnkUj6203MWmHQjRW6sPju6mv/iKX7mYOoCD2SVODKwu+YV1ben5lU=|ckYNjw3OuKPo6dnY|08|3',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://account.seller.shopee.com',
        'priority': 'u=1, i',
        'referer': 'https://account.seller.shopee.com/signin/oauth/identifier?account_type=2&client_id=f9ffc83459897a13dd14c537e84b1753&login_types=%5B1,2,3,4,5%5D&redirect_uri=https%3A%2F%2Fid.xiapibuy.com%2Fapi%2Fseller_platform%2Fnonce%2Fcallback%2F&region=ID&require_passwd=true&response_type=tob_nonce&scope=profile&state=eyJuZXh0IjoiaHR0cHM6Ly9pZC54aWFwaWJ1eS5jb20vIn0%3D',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'x-sec-dfp': 'undefined',
        'x-sz-sdk-version': '3.4.1-2&1.5.6',
        # 'cookie': '_QPWSDCXHZQA=4769076e-9b5d-4918-b1d1-827ac3166dd6; REC7iLP4Q=bf29af4b-6025-4cc8-b8ce-7534c84203f8; SPC_SEC_SI=v1-ZFBzeFlKcVY3ZmdGYUhqYuG94qntLgMzchyCQfG+Ad3J6ljhXBHKznnOrTHiQGgpr3GQ5+sh8bE5Feqmxuozi2pljtkOAf1LUY/a/ZJTJGw=; SPC_SI=3ddyaQAAAABxNVVzN2lQej3lhgcAAAAAQUJiWGZtNjM=; SPC_F=duvWxnwKIarmRhnYfZJQChOKFMsGgMxJ; SC_DFP=WbAhlyqTunwSAUugbfThXjWcmiWtHjFl; osid.f9ffc83459897a13dd14c537e84b1753=1b88a83f67a005f02ed4c046de9587cd; shopee_webUnique_ccd=ivLtK4ve47txnhWdxvQgZg%3D%3D%7CcWjWZ0aI3YAhauaJcpg74VimNMnkUj6203MWmHMjRW6sPju6mv%2FiKX7mYOoCD2SVODKwu%2BYV1ben5lU%3D%7CckYNjw3OuKPo6dnY%7C08%7C3; ds=ca76e8f5a7ff76bee5d5d803ef005a82',
    }

    password_hash = cxt.call('generatePasswordHash', password, 'shop')
    print(f'password_hash: {password_hash}')


    data = {
        'captcha_signature': '',
        'remember': 'false',
        'password_hash': f'{password_hash}',
        'username': f'{username}',
    }

    response = requests.post(
        'https://account.seller.shopee.com/api/account/login/?account_type=2&client_id=f9ffc83459897a13dd14c537e84b1753&login_types=[1,2,3,4,5]&redirect_uri=https:%2F%2Fid.xiapibuy.com%2Fapi%2Fseller_platform%2Fnonce%2Fcallback%2F&region=ID&require_passwd=true&response_type=tob_nonce&scope=profile&state=eyJuZXh0IjoiaHR0cHM6Ly9pZC54aWFwaWJ1eS5jb20vIn0%3D',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(f'status_code: {response.status_code}')
    print(response.json())

if __name__ == '__main__':
    api_account_login('ooo22111', 'qweasd11')
