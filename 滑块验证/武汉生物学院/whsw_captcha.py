# -*- coding: utf-8 -*-
# @File   :whsw_captcha.py
# @Time   :2024/12/19 15:18
# @Author :admin

import requests
import time
import re
import hashlib
import uuid
import ddddocr


class WhswCaptcha:
    def __init__(self):
        self.headers = {
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
        self.det = ddddocr.DdddOcr(det=False, show_ad=False, ocr=False)
        self.session = requests.session()

    def request(self, url, params=None, data=None, method='get', **kwargs):
        if method == 'get':
            return self.session.get(url, params=params, headers=self.headers, **kwargs)
        elif method == 'post':
            return self.session.post(url, data=data, headers=self.headers, **kwargs)
        return None

    def md5_encrypt(self, text):
        """
            将给定的文本转换为MD5哈希值。

            参数:
                text (str): 需要转换的原始文本。

            返回:
                str: 文本的MD5哈希值。
            """
        # 创建一个md5对象
        md5 = hashlib.md5()

        # 使用update方法更新md5对象，注意需要将字符串转为字节串
        md5.update(text.encode('utf-8'))

        # 通过hexdigest方法获取16进制的哈希值
        return md5.hexdigest()

    def get_captcha(self):
        url = 'https://captcha.chaoxing.com/captcha/get/conf'
        params = {
            'callback': 'cx_captcha_function',
            'captchaId': 'qDG21VMg9qS5Rcok4cfpnHGnpf5LhcAv',
            '_': f'{round(time.time(), 2) * 1000}',
        }

        response = self.request(url, params=params).text
        server_time = re.findall(r'"t":(\d+)', response)[0]
        captchaId = re.findall(r'"captchaId":"(.+?)"', response)[0]

        uuid_text = uuid.uuid4()

        captchaKey = self.md5_encrypt(f'{server_time}{uuid_text}')
        token = self.md5_encrypt(server_time + captchaId + 'slide' + captchaKey) + ':' + str(
            (int(server_time) + 300000))
        iv = self.md5_encrypt(captchaId + 'slide' + str(round(time.time(), 2) * 1000) + str(uuid.uuid4()))

        url = 'https://captcha.chaoxing.com/captcha/get/verification/image'
        params = {
            'callback': 'cx_captcha_function',
            'captchaId': f'{captchaId}',
            'type': 'slide',
            'version': '1.1.20',
            'captchaKey': f'{captchaKey}',
            'token': f'{token}',
            'referer': 'https://authserver.whsw.cn/cas/login?service=https%3A%2F%2Fwhsw.hall.chaoxing.com%2Fcas-login%3Fredirect%3D%2Fhome',
            'iv': f'{iv}',
            '_': f'{round(time.time(), 2) * 1000}',
        }
        response = self.request(url, params=params).text
        bg_url = re.findall('"shadeImage":"(.*?)"', response)[0]
        slide_url = re.findall('"cutoutImage":"(.*?)"', response)[0]
        token = re.findall('"token":"(.*?)"', response)[0]

        distance = self.get_distance(bg_url, slide_url)
        print(distance)
        self.verification_captcha(captchaId, iv, distance, token)

    def get_distance(self, bg_url, slide_url):
        slide_image = self.request(slide_url).content
        bg_image = self.request(bg_url).content
        slide = self.det.slide_match(slide_image, bg_image, simple_target=True)
        distance = slide['target'][0]
        return distance

    def verification_captcha(self, captchaId, iv, distance, token):
        params = {
            'callback': 'cx_captcha_function',
            'captchaId': f'{captchaId}',
            'type': 'slide',
            'token': f'{token}',
            'textClickArr': '[{"x":%d}]' % distance,
            'coordinate': '[]',
            'runEnv': '10',
            'version': '1.1.20',
            't': 'a',
            'iv': f'{iv}',
            '_': f'{round(time.time(), 2) * 1000}',
        }
        url = 'https://captcha.chaoxing.com/captcha/check/verification/result'
        response = self.request(url, params=params)
        print(response.text)


if __name__ == '__main__':
    w = WhswCaptcha()
    w.get_captcha()
