# -*- coding: utf-8 -*-
# @File   :api_sign_in.py
# @Time   :2026/1/28 17:23
# @Author :admin

import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')


import execjs


js_code = open('web_pack_dewu.js', 'r', encoding='utf-8')
js_code = js_code.read()
ctx = execjs.compile(js_code)

def api_sign_in(username='18669363933', password='qweasd110'):
    import requests

    cookies = {
        'fe_sensors_ssid': 'c9309750-591d-4b2b-b6d7-643a693fb581',
        'language': 'en',
        '_gcl_au': '1.1.417895653.1769590451',
        'sajssdk_2015_cross_new_user': '1',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2219c03cf6e4e18e-007a10b72b0d8e14-26061d51-2073600-19c03cf6e4f43e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTljMDNjZjZlNGUxOGUtMDA3YTEwYjcyYjBkOGUxNC0yNjA2MWQ1MS0yMDczNjAwLTE5YzAzY2Y2ZTRmNDNlIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219c03cf6e4e18e-007a10b72b0d8e14-26061d51-2073600-19c03cf6e4f43e%22%7D',
        'sk': '9TxgSN1E03VR7SgLtSAH3GZbBP3Hdc0Urzckjq1Kc1V8g6OjxoMsyGAQBQYiIvjutoqn8WscLXUJg5VVd7Z1RtEews1v',
        '_ee_channel': '',
        '_ee_platform': 'pc',
        '_ee_channel_data': '',
        '_ee_timestamp': '1769591357487',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'zh-CN,zh;q=0.9',
        'appid': 'h5',
        'cache-control': 'no-cache',
        'channel': 'pc',
        'clientid': 'global',
        'content-type': 'application/json;charset=UTF-8',
        'deviceid': '7f8721f9-343e-c8a0-6097-33268e881650',
        'dutoken': 'undefined',
        'language': 'zh',
        'origin': 'https://seller.poizon.com',
        'platform': 'pc',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://seller.poizon.com/hk',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'subusertype': '',
        'syscode': 'DU_USER_GLOBAL',
        'timezone': 'GMT+08:00',
        'traceparent': '00-f59804076979d28a322898aaaf3d4818-a78552693024ff33-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        # 'cookie': 'fe_sensors_ssid=c9309750-591d-4b2b-b6d7-643a693fb581; language=en; _gcl_au=1.1.417895653.1769590451; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2219c03cf6e4e18e-007a10b72b0d8e14-26061d51-2073600-19c03cf6e4f43e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTljMDNjZjZlNGUxOGUtMDA3YTEwYjcyYjBkOGUxNC0yNjA2MWQ1MS0yMDczNjAwLTE5YzAzY2Y2ZTRmNDNlIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2219c03cf6e4e18e-007a10b72b0d8e14-26061d51-2073600-19c03cf6e4f43e%22%7D; sk=9TxgSN1E03VR7SgLtSAH3GZbBP3Hdc0Urzckjq1Kc1V8g6OjxoMsyGAQBQYiIvjutoqn8WscLXUJg5VVd7Z1RtEews1v; _ee_channel=; _ee_platform=pc; _ee_channel_data=; _ee_timestamp=1769591357487',
    }



    encodePassword = ctx.call('encodePassword', password)
    appPassword = ctx.call('encodeAppPassword', password)

    print(f'encodePassword: {encodePassword}')
    print(f'appPassword: {appPassword}')

    json_data = {
        'areaCode': '+86',
        'mobile': f'{username}',
        'region': 'HK',
        'password': f'{encodePassword}',
        'appPassword': f'{appPassword}',
        'userType': 2,
    }


    sign = ctx.call('getSign', json_data)
    print(f'sign: {sign}')

    params = {
        # 'sign': '0f4e3f121474338329f7f004ff9cc05c',
        'sign': f'{sign}',
    }


    response = requests.post(
        'https://seller.poizon.com/api/v1/h5/gw/bigger/intl/user/sign-in/mobile-pwd',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    print(f'status_code: {response.status_code}')
    print(f'text: {response.text}')

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"areaCode":"+86","mobile":"18669363933","region":"HK","password":"2ea2ee6c446d1834b4289c5a6304630b","appPassword":"5db7c19db9fb27253f1ce76d5abce863","userType":2}'
    # response = requests.post(
    #    'https://seller.poizon.com/api/v1/h5/gw/bigger/intl/user/sign-in/mobile-pwd',
    #    params=params,
    #    cookies=cookies,
    #    headers=headers,
    #    data=data,
    # )



if __name__ == '__main__':
    api_sign_in()
