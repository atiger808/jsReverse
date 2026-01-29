# -*- coding: utf-8 -*-
# @File   :search_zhihu.py
# @Time   :2025/10/19 08:44
# @Author :admin

def search_zhihu():
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
        'BEC': '5ee33e0856ed13c879689106c041a08d',
        'v_m8': 'AUoqHBdHSH1CTFZNV2hUBFMAGwprFhBXQzwXFQVHBzpXVFBXHllrTVFJUDoLBAgGACxtUUYXQFloQ0NdQWhETFJFV25P',
        'Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49': '1760834305',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.zhihu.com/search?type=km_general&q=%E8%A7%81%E9%9B%AA%E6%94%BB%E7%8B%97',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36',
        'x-api-version': '3.0.91',
        'x-app-za': 'OS=Web',
        'x-requested-with': 'fetch',
        'x-zse-93': '101_3_3.0',
        'x-zse-96': '2.0_FF8tuhuexxZbgZOuevobcVLlbZ6d5uNK1N7M027m0CAyyi1Jrudvrh9WfKF=Sm7a',
        # 'cookie': '_xsrf=w7yznTRws8JYyrdYFcnA7a6ij5wTiRUY; _zap=c4ccb698-2872-429d-a7c5-45ba318cc159; d_c0=JvcT-mw-0BqPToEiZpDBMt5fLv1EtCgKTRs=|1753431607; HMACCOUNT=6C9CDCDD16F20CA7; q_c1=00db504e8796474294881865a8031f5f|1760756900000|1760756900000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1758330889,1760062640; SESSIONID=uK9SdklmJ4ScV72k0pi6csdbgEi9GNVEPI3rXcTBhUV; JOID=UlwcC0mV4V0zdQ09aydCh_53CuV45KdlahNiXAfd0QNRKTgLDTbppVNzBDFg12eMIPMDxB1VG5KP6NoYl_aK6QU=; osd=U1wUC06U4VUzcgw9YydFhv5_CuJ55K9lbRJiVAfa0ANZKT8KDT7polJzDDFn1meEIPQCxBVVHJOP4NoflvaC6QI=; __zse_ck=004_84Y5bUqJ3K/4qPTbCLyKwUEO=6=oeKOlQ6eswprwMk08=qnMGOfqIbnh0KsCMVCflKk=tUFjjCiS0ZUC2qfllPSWJa3blS9zbAgsIP5E=suwSwBLdOvd1bWhNLcgqc6t-acphiPEB9OnKHAKMtJ0Ftqm7vPORak3LTZ1jr2444TXnxjxRDX8abOXK6cQv/nK5/i9NgVPwPvs0C9xziumgo0eeH+UDHUXWJpziew6uPagBicNdRezeLmr2zWboKhS3; z_c0=2|1:0|10:1760756960|4:z_c0|92:Mi4xRGt2UERRQUFBQUFtOXhQNmJEN1FHaVlBQUFCZ0FsVk40UVRXYVFBWkZaeUxab0hUdjM1N19kWmpOU25UbTM4RjVR|b275229f5cb03cbe5ed9c6eacca7d7b8a07324f4c0eb26abe0709f6ce7102c21; BEC=5ee33e0856ed13c879689106c041a08d; v_m8=AUoqHBdHSH1CTFZNV2hUBFMAGwprFhBXQzwXFQVHBzpXVFBXHllrTVFJUDoLBAgGACxtUUYXQFloQ0NdQWhETFJFV25P; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1760834305',
    }

    params = {
        'gk_version': 'gz-gaokao',
        't': 'km_general',
        'q': '见雪攻狗',
        'correction': '1',
        'offset': '0',
        'limit': '20',
        'filter_fields': '',
        'lc_idx': '0',
        'show_all_topics': '0',
        'search_source': 'Normal',
    }

    response = requests.get('https://www.zhihu.com/api/v4/search_v3', params=params, cookies=cookies, headers=headers)

    print(response.text)

if __name__ == '__main__':
    search_zhihu()
