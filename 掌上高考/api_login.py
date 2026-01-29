# -*- coding: utf-8 -*-
# @File   :api_login.py
# @Time   :2026/1/27 15:44
# @Author :admin

import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs


def get_sign(params):
    with open('gaokao_encrypt.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
        return execjs.compile(js_code).call('encryptSign', params)


def get_signsafe(params):
    with open('gaokao_encrypt.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
        return execjs.compile(js_code).call('encryptSignSafe', params)


def login(data):
    import requests

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://www.gaokao.cn',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.gaokao.cn/',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    }

    print(f'data: {data}')
    sign = get_sign(data)
    print(f'sign: {sign}')
    print(f'sign: {len(sign)}')

    url = f"https://api.zjzw.cn/web/api/?login_regist_from=2&method=2&sign={sign}&uri=apigkcx/api/user/login"

    signsafe = get_signsafe(url)
    print(f'signsafe: {signsafe}')

    json_data = {
        'login_regist_from': 2,
        'method': '2',
        'sign': f'{sign}',
        'signsafe': f'{signsafe}',
        'uri': 'apigkcx/api/user/login',
    }

    response = requests.post(
        f'https://api.zjzw.cn/web/api/?login_regist_from=2&method=2&sign={sign}&uri=apigkcx/api/user/login&signsafe={signsafe}',
        headers=headers,
        json=json_data,
    )

    print(f'status_code: {response.status_code}')
    print(f'text: {response.text}')

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"login_regist_from":2,"method":"2","sign":"5356b123e8e28bbc9c61dc62e71001714836bf9380d123199198416a99efd7302164c076406f40a18f261fd6f69fcd175686fcd1f59e1350cadc4454154e9b60eb3e17eb2fce585612e2936937d781f9d6c1e33d2cacccf198379b447269107cfa321847d31619e47180151c50945573","signsafe":"a58e0e46631defe86940166732f9de17","uri":"apigkcx/api/user/login"}'
    # response = requests.post(
    #    'https://api.zjzw.cn/web/api/?login_regist_from=2&method=2&sign=5356b123e8e28bbc9c61dc62e71001714836bf9380d123199198416a99efd7302164c076406f40a18f261fd6f69fcd175686fcd1f59e1350cadc4454154e9b60eb3e17eb2fce585612e2936937d781f9d6c1e33d2cacccf198379b447269107cfa321847d31619e47180151c50945573&uri=apigkcx/api/user/login&signsafe=a58e0e46631defe86940166732f9de17',
    #    headers=headers,
    #    data=data,
    # )


if __name__ == '__main__':
    data = {
        "phone": "18669363693",
        "password": "qweasd12345678",
        "login_type": 8
    }
    login(data)
