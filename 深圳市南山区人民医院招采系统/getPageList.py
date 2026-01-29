# -*- coding: utf-8 -*-
# @File   :getPageList.py
# @Time   :2026/1/28 15:45
# @Author :admin

"""
CryptoJS aes + JsEncrypt rsa
"""

import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs


js_code = open('./jsCode.js', 'r', encoding='utf-8')
js_code = js_code.read()
js_code = execjs.compile(js_code)




def getPageList(pageNum=1):
    import requests

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://zbcg.sznsyy.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://zbcg.sznsyy.cn/homeNotice',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'aesKey': 'Ki547bvZ+l2YIZZj3Ozvze4+mONwYBxeaJY1COONCbQfE+aTQqtr6ySSY/JJtCUK3mcWPltsUE0U6Y/kVm0Zm3xd+vMlXKz1KdT5qp3HH0v8RYeEsl/79S6iEngUJ6lxR+ObInatclkBMgZk5a48+C3jI6FQ5wqIJNbMRNA4zGc=',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        "noticeName": None,
        "pageNum": pageNum,
        "pageSize": 10,
        "tenderCategory": "6",
        "noticeType": None,
        "tenderClass": None
    }
    json_data = js_code.call('encrypt', data)
    print(f'data_encrypt: {json_data}')

    response = requests.post('https://zbcg.sznsyy.cn/sz/purchaser/public/frontPageAnnouncementList', headers=headers,
                             json=json_data)

    print(f'status_code: {response.status_code}')
    data = response.json()
    print(f'data: {data}')

    data = js_code.call('decrypt', data)
    print(f'data_decrypt: {data}')


    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"content":"MI29Et+fVYD2rUH1ZOsK7uRPttd1vsaxP0avJ8j17rmdgbnpoNSns5xn8viyzmUTwQt6CbSvzx9Qc7iY0fDnOz6TDBooMlnvtbp4c5RtwkVnSx3UgCvXSnHLQqkb/SP2HOTAMR0sVS0DsiRKx787lQ==","aesKey":"Ki547bvZ+l2YIZZj3Ozvze4+mONwYBxeaJY1COONCbQfE+aTQqtr6ySSY/JJtCUK3mcWPltsUE0U6Y/kVm0Zm3xd+vMlXKz1KdT5qp3HH0v8RYeEsl/79S6iEngUJ6lxR+ObInatclkBMgZk5a48+C3jI6FQ5wqIJNbMRNA4zGc="}'
    # response = requests.post('https://zbcg.sznsyy.cn/sz/purchaser/public/frontPageAnnouncementList', headers=headers, data=data)



if __name__ == '__main__':
    getPageList(1)
