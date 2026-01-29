# -*- coding: utf-8 -*-
# @File   :wxvote.py
# @Time   :2025/1/17 10:57
# @Author :admin

import requests
import json


def wx_vote(appid='wx3576505d34e8cde6', Authorization='bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9sb2FkLnNoYW5kaWFudy5jblwvYXBpXC9sb2dpblwvbG9naW4iLCJpYXQiOjE3MzcwODIzMDcsImV4cCI6MTczNzY4NzEwNywibmJmIjoxNzM3MDgyMzA3LCJqdGkiOiJPSURrVW9pMTNpbm5scWVmIiwic3ViIjo1NTYxOTQ3OCwicHJ2IjoiMTI1MWQzYmQ5MjE4MjZkOGYwNzFkNjIzMmZjYjc0MjYxMGM4MTZhYSJ9.cxhFv4TQ1fu5L1z-Si0l9jq4xkmF3vJ7zH1u2u0Oa80'):

    url = 'https://load.shandianw.cn/api/voting_attend/attend'

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',  # 修改为 JSON 格式
        'Authorization': f'{Authorization}',
        'Origin': 'https://192.168.1.1:65534',
        'Referer': f'https://servicewechat.com/{appid}/318/page-frame.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581',
        'Accept-Encoding': 'gzip, deflate, br',
        'multi-id': '1',
        'scene': '1007',
        'xweb_xhr': '1',
        'app-id': f'{appid}',
        'version': '3.0.53',
    }

    data = {
        "activity_id": 472644,
        "group_id": 0,
        "join_id": [4917519],  # 确保是数组格式
        "scene": 1007,
        "form_text": [],
        "score": []
    }

    # 将 data 转换为 JSON 格式
    json_data = json.dumps(data)

    # 打印调试信息
    print("URL:", url)
    print("Headers:", headers)
    print("Data:", json_data)

    # 发送 POST 请求
    res = requests.post(url, data=json_data, headers=headers, verify=False)
    if res.status_code == 200:
        print(res.json())
    else:
        print(res.status_code)
        print(res.text)


h = '''

POST /api/login/login HTTP/1.1
Host: load.shandianw.cn
Connection: keep-alive
Content-Length: 43
Authorization: bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9sb2FkLnNoYW5kaWFudy5jblwvYXBpXC9sb2dpblwvbG9naW4iLCJpYXQiOjE3MzcwODQyMzMsImV4cCI6MTczNzY4OTAzMywibmJmIjoxNzM3MDg0MjMzLCJqdGkiOiI5YTlYTUFTVHdLNW1WZDNFIiwic3ViIjo1NTYxOTQ3OCwicHJ2IjoiMTI1MWQzYmQ5MjE4MjZkOGYwNzFkNjIzMmZjYjc0MjYxMGM4MTZhYSJ9.LiAD2o_AatM1xA8GuSEFGxik_SuENHu4HMvqJ_Axn58
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581
Content-Type: application/json
multi-id: 1
scene: 1007
xweb_xhr: 1
app-id: wx3576505d34e8cde6
version: 3.0.53
Accept: */*
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://servicewechat.com/wx3576505d34e8cde6/318/page-frame.html
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9



'''

def api_login(appid='wx3576505d34e8cde6', Authorization='bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9sb2FkLnNoYW5kaWFudy5jblwvYXBpXC9sb2dpblwvbG9naW4iLCJpYXQiOjE3MzcwODQyMzMsImV4cCI6MTczNzY4OTAzMywibmJmIjoxNzM3MDg0MjMzLCJqdGkiOiI5YTlYTUFTVHdLNW1WZDNFIiwic3ViIjo1NTYxOTQ3OCwicHJ2IjoiMTI1MWQzYmQ5MjE4MjZkOGYwNzFkNjIzMmZjYjc0MjYxMGM4MTZhYSJ9.LiAD2o_AatM1xA8GuSEFGxik_SuENHu4HMvqJ_Axn58'):
    url = 'https://load.shandianw.cn/api/login/login'

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',  # 修改为 JSON 格式
        'Authorization': f'{Authorization}',
        'Referer': f'https://servicewechat.com/{appid}/318/page-frame.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11581',
        'Accept-Encoding': 'gzip, deflate, br',
        'multi-id': '1',
        'scene': '1007',
        'xweb_xhr': '1',
        'app-id': f'{appid}',
        'version': '3.0.53',
        'Host': 'load.shandianw.cn',
    }

    data = {
        "code": '0c1MS8ll2h6OSe4Samml28Jfkf1MS8lk',
    }
    data = {"code":"0c1MS8ll2h6OSe4Samml28Jfkf1MS8lk"}
    data = {"code":"0c1ypZ100hU0AT1dDa200BdsEP1ypZ1S"}
    data = {"code":"071uuz0w3Ewre43bWh1w3Nsavn4uuz0m"}

    # 将 data 转换为 JSON 格式
    json_data = json.dumps(data)

    # 打印调试信息
    print("URL:", url)
    print("Headers:", headers)
    print("Data:", json_data)

    # 发送 POST 请求
    res = requests.post(url, data=json_data, headers=headers, verify=False)
    if res.status_code == 200:
        print(res.json())
    else:
        print(res.status_code)
        print(res.text)





if __name__ == '__main__':
    appid = 'wx3576505d34e8cde6'
    Authorization = 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9sb2FkLnNoYW5kaWFudy5jblwvYXBpXC9sb2dpblwvbG9naW4iLCJpYXQiOjE3MzcwODIzMDcsImV4cCI6MTczNzY4NzEwNywibmJmIjoxNzM3MDgyMzA3LCJqdGkiOiJPSURrVW9pMTNpbm5scWVmIiwic3ViIjo1NTYxOTQ3OCwicHJ2IjoiMTI1MWQzYmQ5MjE4MjZkOGYwNzFkNjIzMmZjYjc0MjYxMGM4MTZhYSJ9.cxhFv4TQ1fu5L1z-Si0l9jq4xkmF3vJ7zH1u2u0Oa80'
    Authorization = 'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9sb2FkLnNoYW5kaWFudy5jblwvYXBpXC9sb2dpblwvbG9naW4iLCJpYXQiOjE3MzcwOTkyOTMsImV4cCI6MTczNzcwNDA5MywibmJmIjoxNzM3MDk5MjkzLCJqdGkiOiI1eXdpdjRUQ3RvdGxOZWRVIiwic3ViIjo1NTYxOTQ3OCwicHJ2IjoiMTI1MWQzYmQ5MjE4MjZkOGYwNzFkNjIzMmZjYjc0MjYxMGM4MTZhYSJ9.J_gI2CJas7_dCYxoRMwNAtKVHW6ZOELu65JsL5rJwEU'

    # api_login(appid=appid, Authorization=Authorization)

    # Authorization = ''
    wx_vote(appid=appid, Authorization=Authorization)
