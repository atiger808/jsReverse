# -*- coding: utf-8 -*-
# @File   :mobileCode_login.py
# @Time   :2026/1/15 14:42
# @Author :admin

import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import requests
import execjs


def get_sign(params):
    with open('codejs_mobileCode_get_sign.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
        return execjs.compile(js_code).call('get_sign', params)


def mobileCode_login(phone, smsCode):


    cookies = {
        'apdid': 'bf3475ed-1888-49ea-9b1e-c4bf263a158d7515064ddce9e793ef415d6bb782069f:1763460001:1',
        'didv': '1766129170000',
        'did': 'web_495d14d68967050dbb98b196bd613294',
        'kwpsecproductname': 'kuaishou-vision',
        'kwscode': '04dc103d63222cfdfec0057c058fb1c4c5f2eb14eefcce98b2a503578e5f8431',
        'kwssectoken': 'kUsc2qrjUrqiGEe5ZsCpZo1Ug1tsasZExSNNEuSPwUwi9RHkP3u4W0oQG5HqgTPTdoyFv9WZpIYYK6HvLESV9g==',
        'kwfv1': 'PnGU+9+Y8008S+nH0U+0mjPf8fP08f+98f+nLlwnrIP9+Sw/ZFGfzY+eGlGf+f+e4SGfbYP0QfGnLFwBLU80mYG9PIwezf+BL7w/zSGAD9G0bj+nQSPBcU80zfPnLU+npf8emY+Br9PfP780HF+/40PBGhPfzjP/G7P9H78nQY+AZ=',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.kuaishou.com',
        'Referer': 'https://www.kuaishou.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'apdid=bf3475ed-1888-49ea-9b1e-c4bf263a158d7515064ddce9e793ef415d6bb782069f:1763460001:1; didv=1766129170000; did=web_495d14d68967050dbb98b196bd613294; kwpsecproductname=kuaishou-vision; kwscode=04dc103d63222cfdfec0057c058fb1c4c5f2eb14eefcce98b2a503578e5f8431; kwssectoken=kUsc2qrjUrqiGEe5ZsCpZo1Ug1tsasZExSNNEuSPwUwi9RHkP3u4W0oQG5HqgTPTdoyFv9WZpIYYK6HvLESV9g==; kwfv1=PnGU+9+Y8008S+nH0U+0mjPf8fP08f+98f+nLlwnrIP9+Sw/ZFGfzY+eGlGf+f+e4SGfbYP0QfGnLFwBLU80mYG9PIwezf+BL7w/zSGAD9G0bj+nQSPBcU80zfPnLU+npf8emY+Br9PfP780HF+/40PBGhPfzjP/G7P9H78nQY+AZ=',
    }

    data = {
        'countryCode': '+86',
        'phone': f'{phone}',
        'sid': 'kuaishou.server.webday7',
        'createId': 'true',
        'smsCode': f'{smsCode}',
        'setCookie': 'true',
        'channelType': 'UNKNOWN',
        'isWebSig4': 'true',
    }

    params = {
        "url": "/pass/kuaishou/login/mobileCode",
        "query": {
            "caver": 2
        },
        "form": {
            "countryCode": "+86",
            "phone": f"{phone}",
            "sid": "kuaishou.server.webday7",
            "createId": True,
            "smsCode": f"{smsCode}",
            "setCookie": True,
            "channelType": "UNKNOWN",
            "isWebSig4": True
        },
        "requestBody": {},
        "projectInfo": {
            "appKey": "q5yq4bjUut",
            "radarId": "0abb8037ac"
        }
    }

    sign = get_sign(params)

    print(f'sign:: {sign}')



    response = requests.post(
        f'https://id.kuaishou.com/pass/kuaishou/login/mobileCode?__NS_hxfalcon={sign}&caver=2',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    print(response.json())
    return response.json()


if __name__ == '__main__':
    mobileCode_login(phone='18669636663', smsCode='556632')
