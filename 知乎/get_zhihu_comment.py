# -*- coding: utf-8 -*-
# @File   :get_zhihu_comment.py
# @Time   :2025/10/18 14:22
# @Author :admin
import execjs

import time
import requests

import execjs

def get_sign(params):
    with open('get_x-zse-96.js', 'r', encoding='utf-8') as f:
        jscode = f.read()
    return execjs.compile(jscode).call('get_x_zse_96', params)


def get_comment():
    import requests

    cookies = {
        '_xsrf': 'w7yznTRws8JYyrdYFcnA7a6ij5wTiRUY',
        '_zap': 'c4ccb698-2872-429d-a7c5-45ba318cc159',
        'd_c0': 'JvcT-mw-0BqPToEiZpDBMt5fLv1EtCgKTRs=|1753431607',
        'HMACCOUNT': '6C9CDCDD16F20CA7',
        'q_c1': '00db504e8796474294881865a8031f5f|1760756900000|1760756900000',
        'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49': '1758330889,1760062640',
        'SESSIONID': 'uK9SdklmJ4ScV72k0pi6csdbgEi9GNVEPI3rXcTBhUV',
        'JOID': 'UlwcC0mV4V0zdQ09aydCh_53CuV45KdlahNiXAfd0QNRKTgLDTbppVNzBDFg12eMIPMDxB1VG5KP6NoYl_aK6QU=',
        'osd': 'U1wUC06U4VUzcgw9YydFhv5_CuJ55K9lbRJiVAfa0ANZKT8KDT7polJzDDFn1meEIPQCxBVVHJOP4NoflvaC6QI=',
        '__zse_ck': '004_84Y5bUqJ3K/4qPTbCLyKwUEO=6=oeKOlQ6eswprwMk08=qnMGOfqIbnh0KsCMVCflKk=tUFjjCiS0ZUC2qfllPSWJa3blS9zbAgsIP5E=suwSwBLdOvd1bWhNLcgqc6t-acphiPEB9OnKHAKMtJ0Ftqm7vPORak3LTZ1jr2444TXnxjxRDX8abOXK6cQv/nK5/i9NgVPwPvs0C9xziumgo0eeH+UDHUXWJpziew6uPagBicNdRezeLmr2zWboKhS3',
        'z_c0': '2|1:0|10:1760756960|4:z_c0|92:Mi4xRGt2UERRQUFBQUFtOXhQNmJEN1FHaVlBQUFCZ0FsVk40UVRXYVFBWkZaeUxab0hUdjM1N19kWmpOU25UbTM4RjVR|b275229f5cb03cbe5ed9c6eacca7d7b8a07324f4c0eb26abe0709f6ce7102c21',
        'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1760767520',
        'BEC': '6c53268835aec2199978cd4b4f988f8c',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.zhihu.com/question/278775655/answer/1957944208330564910',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'x-requested-with': 'fetch',
        'x-zse-93': '101_3_3.0',
        'x-zse-96': '2.0_xkvAAi00ikzfWI0CmesCMrzmpbulmBhL+jTMoMZ4DrhACkQQk3h21ZDevR1/jUUQ',
        # 'cookie': '_xsrf=w7yznTRws8JYyrdYFcnA7a6ij5wTiRUY; _zap=c4ccb698-2872-429d-a7c5-45ba318cc159; d_c0=JvcT-mw-0BqPToEiZpDBMt5fLv1EtCgKTRs=|1753431607; HMACCOUNT=6C9CDCDD16F20CA7; q_c1=00db504e8796474294881865a8031f5f|1760756900000|1760756900000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1758330889,1760062640; SESSIONID=uK9SdklmJ4ScV72k0pi6csdbgEi9GNVEPI3rXcTBhUV; JOID=UlwcC0mV4V0zdQ09aydCh_53CuV45KdlahNiXAfd0QNRKTgLDTbppVNzBDFg12eMIPMDxB1VG5KP6NoYl_aK6QU=; osd=U1wUC06U4VUzcgw9YydFhv5_CuJ55K9lbRJiVAfa0ANZKT8KDT7polJzDDFn1meEIPQCxBVVHJOP4NoflvaC6QI=; __zse_ck=004_84Y5bUqJ3K/4qPTbCLyKwUEO=6=oeKOlQ6eswprwMk08=qnMGOfqIbnh0KsCMVCflKk=tUFjjCiS0ZUC2qfllPSWJa3blS9zbAgsIP5E=suwSwBLdOvd1bWhNLcgqc6t-acphiPEB9OnKHAKMtJ0Ftqm7vPORak3LTZ1jr2444TXnxjxRDX8abOXK6cQv/nK5/i9NgVPwPvs0C9xziumgo0eeH+UDHUXWJpziew6uPagBicNdRezeLmr2zWboKhS3; z_c0=2|1:0|10:1760756960|4:z_c0|92:Mi4xRGt2UERRQUFBQUFtOXhQNmJEN1FHaVlBQUFCZ0FsVk40UVRXYVFBWkZaeUxab0hUdjM1N19kWmpOU25UbTM4RjVR|b275229f5cb03cbe5ed9c6eacca7d7b8a07324f4c0eb26abe0709f6ce7102c21; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1760767520; BEC=6c53268835aec2199978cd4b4f988f8c',
    }






    order_by = 'score'
    limit = '20'
    offset = '1653692670_11308543881_1'

    ta = "101_3_3.0"
    tp = f"/api/v4/comment_v5/answers/1957944208330564910/root_comment?order_by={order_by}&limit={limit}&offset={offset}"
    tu = "JvcT-mw-0BqPToEiZpDBMt5fLv1EtCgKTRs=|1753431607"

    s = '+'.join([ta, tp, tu,])
    print(s)
    sign = get_sign(s)
    print(sign)
    print(len(sign))
    headers['x-zse-96'] =  sign
    response = requests.get(
        f'https://www.zhihu.com{tp}',
        cookies=cookies,
        headers=headers,
    )
    print(response.text)


if __name__ == '__main__':
    get_comment()
