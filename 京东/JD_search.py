# -*- coding: utf-8 -*-
# @File   :JD_search.py
# @Time   :2025/10/11 15:17
# @Author :admin

import json
import time
import requests
from hashlib import sha256


def sha256_hash(string):
    return sha256(string.encode('utf-8')).hexdigest()


body = {
    "page": 1,
    "pagesize": 25,
    "area": "15_1262_0_0",
    "source": "pc-home",
    "gb": 1
}

params = {
    "appid": "www-jd-com",
    "body": sha256_hash(json.dumps(body)),
    "clientVersion": "1.0.0",
    "client": "pc",
    "functionId": "pc_home_feed",
    "t": int(time.time() * 1000)
}

print(f'params: {params}')

response = requests.post('http://localhost:3000/api/data', json={"params": params})

param = response.json()['result']

print(param)
print(len(param['h5st']))

cookies = {
    'unpl': 'JF8EALBnNSttXBxdUhkLTBoQH15UW1gATx4EPTUNBltcSVZWHlYTE0d7XlVdWRRLFh9vZhRVVVNKXA4bCysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAh8aEENbXFZVAHsWM2hXNWRdUUlUARgyGiIRex8AAl8NTBAKaioFUFVYQ1INEwoTIhF7Xg',
    '__jdc': '76161171',
    '__jdu': '1591979999',
    '3AB9D23F7A4B3C9B': 'JRH3QUKHXXIFE26JHB5KRTP3WHN2JMEMOWD5A5ZPUDZECHWNKK4TRM25UDONDILNXWJPY3EFSWPVW64OES36OZAI3Q',
    'areaId': '15',
    'ipLoc-djd': '15-1262-0-0',
    'PCSYCityID': 'CN_330000_330700_0',
    'shshshfpa': '6bf509f2-3513-e39e-9416-fb8b9fd86aa7-1760058602',
    'shshshfpx': '6bf509f2-3513-e39e-9416-fb8b9fd86aa7-1760058602',
    '3AB9D23F7A4B3CSS': 'jdd03JRH3QUKHXXIFE26JHB5KRTP3WHN2JMEMOWD5A5ZPUDZECHWNKK4TRM25UDONDILNXWJPY3EFSWPVW64OES36OZAI3QAAAAMZZUEWARAAAAAADQ7S3IKALMIXZ4X',
    'shshshfpb': 'BApXS-ZQCzvxAA6fix1QNKibfkvwkHtt9BiJEgS1o9xJ1Mk9n9Y62',
    '__jda': '76161171.1591979999.1760058559.1760151945.1760161520.7',
    '__jdb': '76161171.36.1591979999|7.1760161520',
    '__jdv': '76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_5f8f38f91e21449586cc9c7533b4e90f|1760167174862',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www.jd.com/',
    'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
    'cookie': 'unpl=JF8EALBnNSttXBxdUhkLTBoQH15UW1gATx4EPTUNBltcSVZWHlYTE0d7XlVdWRRLFh9vZhRVVVNKXA4bCysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAh8aEENbXFZVAHsWM2hXNWRdUUlUARgyGiIRex8AAl8NTBAKaioFUFVYQ1INEwoTIhF7Xg; __jdu=1591979999; areaId=15; ipLoc-djd=15-1262-0-0; PCSYCityID=CN_330000_330700_0; shshshfpa=6bf509f2-3513-e39e-9416-fb8b9fd86aa7-1760058602; shshshfpx=6bf509f2-3513-e39e-9416-fb8b9fd86aa7-1760058602; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_5f8f38f91e21449586cc9c7533b4e90f|1760170640793; 3AB9D23F7A4B3CSS=jdd03JRH3QUKHXXIFE26JHB5KRTP3WHN2JMEMOWD5A5ZPUDZECHWNKK4TRM25UDONDILNXWJPY3EFSWPVW64OES36OZAI3QAAAAMZ2JMP4SQAAAAADHFNSAYUDX7YB4X; wlfstk_smdl=wdd5txjyo5c18npqh1ute6253ycygg7d; 3AB9D23F7A4B3C9B=JRH3QUKHXXIFE26JHB5KRTP3WHN2JMEMOWD5A5ZPUDZECHWNKK4TRM25UDONDILNXWJPY3EFSWPVW64OES36OZAI3Q; __jda=76161171.1591979999.1760058559.1760151945.1760161520.7; __jdc=76161171; shshshfpb=BApXSZ8dR0fxAA6fix1QNKibfkvwkHtt9BiJEgS1p9xJ1Mk9n9Y62; __jdb=76161171.53.1591979999|7.1760161520; sdtoken=AAbEsBpEIOVjqTAKCQtvQu17MXf2dwp661I7uJGDhNNirPNMiUROnbJbFTASsSkGrJOCm_z3BpXHIzpUCU4eDlmAac5VteJoyjQqY-Y1sTe5yMEgMMpNWJXN-LOK9ahCAJUFHZM9pMWWrpjWkZbY'
}

params = {
    'appid': 'www-jd-com',
    'body': json.dumps(body),
    'clientVersion': '1.0.0',
    'client': 'pc',
    'functionId': 'pc_home_feed',
    't': param['t'],
    'uuid': '76161171.1591979999.1760058559.1760151945.1760161520.7',
    'loginType': '3',
    'x-api-eid-token': 'jdd03JRH3QUKHXXIFE26JHB5KRTP3WHN2JMEMOWD5A5ZPUDZECHWNKK4TRM25UDONDILNXWJPY3EFSWPVW64OES36OZAI3QAAAAMZ2JMP4SQAAAAADHFNSAYUDX7YB4X',
    'callback': 'jsonpMore2Goods',
    '_': int(time.time() * 1000),
    'h5st': param['h5st'],
}

print(f'params2: {params}')

response = requests.get('https://api.m.jd.com/', params=params, headers=headers)
print('status_code: ', response.status_code)
print('result: ', response.text)

# if __name__ == '__main__':
#     pass
