# -*- coding: utf-8 -*-
# @File   :toutiao_feed.py
# @Time   :2024/12/18 15:03
# @Author :admin

import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
from urllib.parse import urlencode

def get_a_bogus(params):
    with open('jsCode_toutiao_get_a_b.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
    return execjs.compile(js_code).call('get_a_b', params)


def feed_data():
    import requests

    cookies = {
        '__ac_signature': '_02B4Z6wo00f01O6GytwAAIDBMv9VaLmbRYzups5AAF1228',
        'tt_webid': '7408760620617123328',
        'ttcid': 'f1580be8f6774a43a6696224beb38f7a35',
        'csrftoken': '0bbb3ce1e6cc3e3cd0fcfb0cabab2875',
        '_ga': 'GA1.1.601199123.1724986535',
        '_S_DPR': '1',
        '_S_IPAD': '0',
        '_tea_utm_cache_24': '{%22utm_medium%22:%22wap_search%22}',
        '_tea_utm_cache_2018': '{%22utm_medium%22:%22wap_search%22}',
        'n_mh': 'XK1o04PTRKaJrX31mB4DX2LQOUHNGQ6_8bBYhoc6zlE',
        'store-region': 'cn-bj',
        'store-region-src': 'uid',
        's_v_web_id': 'verify_m2wnb0y4_ndTxahHW_tphm_408i_AAPR_m0fImeeRImqk',
        'passport_csrf_token': 'b35d28863dbdbe7708370d6beb828423',
        'passport_csrf_token_default': 'b35d28863dbdbe7708370d6beb828423',
        'sso_uid_tt': 'e57a6c5ef20d226158db893d2f52a276',
        'sso_uid_tt_ss': 'e57a6c5ef20d226158db893d2f52a276',
        'toutiao_sso_user': 'af4d7de673837ff226fe285ec5d4358d',
        'toutiao_sso_user_ss': 'af4d7de673837ff226fe285ec5d4358d',
        'sid_ucp_sso_v1': '1.0.0-KDExZTZkMTk5YWVjZWIwNGI1MDFhNDdmNTEwNTc1ZDlmNTdiNzYwYTcKHgjombDZxfXcAhCgldW5BhgYIAww6uaW5gU4BkD0BxoCaGwiIGFmNGQ3ZGU2NzM4MzdmZjIyNmZlMjg1ZWM1ZDQzNThk',
        'ssid_ucp_sso_v1': '1.0.0-KDExZTZkMTk5YWVjZWIwNGI1MDFhNDdmNTEwNTc1ZDlmNTdiNzYwYTcKHgjombDZxfXcAhCgldW5BhgYIAww6uaW5gU4BkD0BxoCaGwiIGFmNGQ3ZGU2NzM4MzdmZjIyNmZlMjg1ZWM1ZDQzNThk',
        'sid_guard': '824b8a2e733fa52d6a9b64674259c5f6%7C1731545761%7C5184001%7CMon%2C+13-Jan-2025+00%3A56%3A02+GMT',
        'uid_tt': 'bbc7388b2a78f73aaf16f1bec0b5f520',
        'uid_tt_ss': 'bbc7388b2a78f73aaf16f1bec0b5f520',
        'sid_tt': '824b8a2e733fa52d6a9b64674259c5f6',
        'sessionid': '824b8a2e733fa52d6a9b64674259c5f6',
        'sessionid_ss': '824b8a2e733fa52d6a9b64674259c5f6',
        'is_staff_user': 'false',
        'sid_ucp_v1': '1.0.0-KGUzOWY2ZjZhNmJhODM4MDQ0MWZjZmMyNjU2ZWFjZjI1MmNhNzJjNWUKGAjombDZxfXcAhChldW5BhgYIAw4BkD0BxoCbHEiIDgyNGI4YTJlNzMzZmE1MmQ2YTliNjQ2NzQyNTljNWY2',
        'ssid_ucp_v1': '1.0.0-KGUzOWY2ZjZhNmJhODM4MDQ0MWZjZmMyNjU2ZWFjZjI1MmNhNzJjNWUKGAjombDZxfXcAhChldW5BhgYIAw4BkD0BxoCbHEiIDgyNGI4YTJlNzMzZmE1MmQ2YTliNjQ2NzQyNTljNWY2',
        'csrf_session_id': 'd4bfad3988bdc781fc0172626ea2d12b',
        'local_city_cache': '%E8%AE%B8%E6%98%8C',
        'odin_tt': 'ccfed943ed2fa5a19599cccddbaec6a939fbd79f328c4b2fc6bd3adfccbd17946e6d06b58d8e8c2eab9edee952de0a89',
        '_S_WIN_WH': '1920_919',
        'gfkadpd': '24,6457',
        'tt_anti_token': 'homBHkuPHRc-9a6354790477c3dca253fe233f77535b4220b80d1b96efabafcea321340ea29a',
        '_ga_QEHZPBE5HH': 'GS1.1.1734503727.129.1.1734504270.0.0.0',
        'tt_scid': '7SMCV5yF5CJ.x1--v1C1GkJABA00aWAUhIp4vs1p7dfwjgB3i.P.gL0mNHBblQeqeaa3',
        'ttwid': '1%7CPlRkVzwhsgGYzYieJ427vDDMos1v0j1uqCCPns6--sE%7C1734505267%7C74212350c36b555e595245149e5b9025dfb48d1638b6b2ee5cf0b0e50253c9e5',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': '__ac_signature=_02B4Z6wo00f01O6GytwAAIDBMv9VaLmbRYzups5AAF1228; tt_webid=7408760620617123328; ttcid=f1580be8f6774a43a6696224beb38f7a35; csrftoken=0bbb3ce1e6cc3e3cd0fcfb0cabab2875; _ga=GA1.1.601199123.1724986535; _S_DPR=1; _S_IPAD=0; _tea_utm_cache_24={%22utm_medium%22:%22wap_search%22}; _tea_utm_cache_2018={%22utm_medium%22:%22wap_search%22}; n_mh=XK1o04PTRKaJrX31mB4DX2LQOUHNGQ6_8bBYhoc6zlE; store-region=cn-bj; store-region-src=uid; s_v_web_id=verify_m2wnb0y4_ndTxahHW_tphm_408i_AAPR_m0fImeeRImqk; passport_csrf_token=b35d28863dbdbe7708370d6beb828423; passport_csrf_token_default=b35d28863dbdbe7708370d6beb828423; sso_uid_tt=e57a6c5ef20d226158db893d2f52a276; sso_uid_tt_ss=e57a6c5ef20d226158db893d2f52a276; toutiao_sso_user=af4d7de673837ff226fe285ec5d4358d; toutiao_sso_user_ss=af4d7de673837ff226fe285ec5d4358d; sid_ucp_sso_v1=1.0.0-KDExZTZkMTk5YWVjZWIwNGI1MDFhNDdmNTEwNTc1ZDlmNTdiNzYwYTcKHgjombDZxfXcAhCgldW5BhgYIAww6uaW5gU4BkD0BxoCaGwiIGFmNGQ3ZGU2NzM4MzdmZjIyNmZlMjg1ZWM1ZDQzNThk; ssid_ucp_sso_v1=1.0.0-KDExZTZkMTk5YWVjZWIwNGI1MDFhNDdmNTEwNTc1ZDlmNTdiNzYwYTcKHgjombDZxfXcAhCgldW5BhgYIAww6uaW5gU4BkD0BxoCaGwiIGFmNGQ3ZGU2NzM4MzdmZjIyNmZlMjg1ZWM1ZDQzNThk; sid_guard=824b8a2e733fa52d6a9b64674259c5f6%7C1731545761%7C5184001%7CMon%2C+13-Jan-2025+00%3A56%3A02+GMT; uid_tt=bbc7388b2a78f73aaf16f1bec0b5f520; uid_tt_ss=bbc7388b2a78f73aaf16f1bec0b5f520; sid_tt=824b8a2e733fa52d6a9b64674259c5f6; sessionid=824b8a2e733fa52d6a9b64674259c5f6; sessionid_ss=824b8a2e733fa52d6a9b64674259c5f6; is_staff_user=false; sid_ucp_v1=1.0.0-KGUzOWY2ZjZhNmJhODM4MDQ0MWZjZmMyNjU2ZWFjZjI1MmNhNzJjNWUKGAjombDZxfXcAhChldW5BhgYIAw4BkD0BxoCbHEiIDgyNGI4YTJlNzMzZmE1MmQ2YTliNjQ2NzQyNTljNWY2; ssid_ucp_v1=1.0.0-KGUzOWY2ZjZhNmJhODM4MDQ0MWZjZmMyNjU2ZWFjZjI1MmNhNzJjNWUKGAjombDZxfXcAhChldW5BhgYIAw4BkD0BxoCbHEiIDgyNGI4YTJlNzMzZmE1MmQ2YTliNjQ2NzQyNTljNWY2; csrf_session_id=d4bfad3988bdc781fc0172626ea2d12b; local_city_cache=%E8%AE%B8%E6%98%8C; odin_tt=ccfed943ed2fa5a19599cccddbaec6a939fbd79f328c4b2fc6bd3adfccbd17946e6d06b58d8e8c2eab9edee952de0a89; _S_WIN_WH=1920_919; gfkadpd=24,6457; tt_anti_token=homBHkuPHRc-9a6354790477c3dca253fe233f77535b4220b80d1b96efabafcea321340ea29a; _ga_QEHZPBE5HH=GS1.1.1734503727.129.1.1734504270.0.0.0; tt_scid=7SMCV5yF5CJ.x1--v1C1GkJABA00aWAUhIp4vs1p7dfwjgB3i.P.gL0mNHBblQeqeaa3; ttwid=1%7CPlRkVzwhsgGYzYieJ427vDDMos1v0j1uqCCPns6--sE%7C1734505267%7C74212350c36b555e595245149e5b9025dfb48d1638b6b2ee5cf0b0e50253c9e5',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://www.toutiao.com/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    params = {
        'channel_id': '0',
        'min_behot_time': '1734504266',
        'offset': '0',
        'refresh_count': '2',
        'category': 'pc_profile_recommend',
        'aid': '24',
        'app_name': 'toutiao_web',
        'msToken': 'SOPWs2o1Ag0i-8a4tIKeYLG0PJFz8ixpjyBlrGJb_jpbWXhAxE2swZt18cNPycMN-azwl-nefoz96-MQkIzEuUASMdHEo4nUxPEVxFHAnsExL2ljpuqC-mLgA7EfA7aG',
        # 'a_bogus': 'x68wQmhDDkIPff6Z5XnLfY3qVve3Y8ei0t9bMDhqndViw639HMT69exE3Swv1U8jNG/pIe8jy4hbO3xprQVGMZwf7Wsx/2CZsg00t-P2sogS53iJeyUgrUwi-hsASePQsv1IEQfkqwArFuRDWoKjmhKRTfxja3Lk96EtrNqL2o0T',
    }

    a_bogus = get_a_bogus(urlencode(params))
    print(f'a_bogus: {a_bogus}')
    print(len(a_bogus))
    params['a_bogus'] = a_bogus
    response = requests.get('https://www.toutiao.com/api/pc/list/feed', params=params, cookies=cookies, headers=headers)
    print(response.text)
    result = response.json()
    print(result)

if __name__ == '__main__':
    feed_data()
