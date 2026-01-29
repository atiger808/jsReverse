# -*- coding: utf-8 -*-
# @File   :api_login.py
# @Time   :2026/1/28 16:40
# @Author :admin


import requests
import execjs

session = requests.session()


js_code = open('./jsCode.js', 'r', encoding='utf-8')
js_code = js_code.read()
ctx = execjs.compile(js_code)



def api_login(username='18693639363', password='qwe123'):


    cookies = {
        '_bl_uid': 'jpm64kwFc89526w8X0yvlF5vwU4j',
        'HOLDONKEY': 'NzE5YzQxMDEtMzBmZC00NWE4LWJiMDMtMDNlNGUxYmYwZDMw',
        'ncCookie': '5loK4768DIfAq3w1J694XQpiBOfvWTcyr_LKrBhxpgen5ZOS2ieWO08DKhhoS089B1y5eCCVdzrR2VVNTVi-2SHjEhXqFsoOUL1wsnXzevZm4I9Yc6H80w9fSXzyhqBM',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://account.court.gov.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://account.court.gov.cn/app?back_url=https%3A%2F%2Faccount.court.gov.cn%2Foauth%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3Dzgcpwsw%26redirect_uri%3Dhttps%253A%252F%252Fwenshu.court.gov.cn%252FCallBackController%252FauthorizeCallBack%26state%3D6bd168e1-02a0-498e-b6ad-37d92502aae4%26timestamp%3D1769587455707%26signature%3D07E92E930295E36995CAFE6E83B74D62F5020D075BC7DAF7A3789D0E190A5DB4%26scope%3Duserinfo',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': '_bl_uid=jpm64kwFc89526w8X0yvlF5vwU4j; HOLDONKEY=NzE5YzQxMDEtMzBmZC00NWE4LWJiMDMtMDNlNGUxYmYwZDMw; ncCookie=5loK4768DIfAq3w1J694XQpiBOfvWTcyr_LKrBhxpgen5ZOS2ieWO08DKhhoS089B1y5eCCVdzrR2VVNTVi-2SHjEhXqFsoOUL1wsnXzevZm4I9Yc6H80w9fSXzyhqBM',
    }

    password = ctx.call('encodePassword', password)
    print(f'password: {password}')

    data = {
        'username': '18693639363',
        'password': password,
        'bizToken': '6cd4605e-d487-4870-9ffb-ce0aa8866440',
        'imgVerifyToken': '6cd4605e-d487-4870-9ffb-ce0aa8866440',
        'appDomain': 'wenshu.court.gov.cn',
    }

    response = session.post('https://account.court.gov.cn/api/login', cookies=cookies, headers=headers, data=data)

    print(f'status_code: {response.status_code}')
    print(response.json())


if __name__ == '__main__':
    api_login()
