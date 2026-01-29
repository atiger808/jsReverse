# -*- coding: utf-8 -*-
# @File   :dy_captcha_slider.py
# @Time   :2024/12/18 16:32
# @Author :admin

import subprocess
from functools import partial
from idlelib.iomenu import encoding

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs

import requests
import cv2
import json
import random

class DouyinCaptchaSlider:
    def __init__(self, url, cookies, headers):
        self.url = url
        self.cookies = cookies
        self.headers = headers
        self.session = requests.session()
        self.session.headers.update(self.headers)
        self.session.cookies.update(self.cookies)
        self.token = self.get_token()

    def identify(self):
        bg_img = cv2.imread('bg.jpg')
        slice_img = cv2.imread('slice.png')

        bg = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
        slice = cv2.cvtColor(slice_img, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(bg, slice, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        return max_loc[0]

    def get_tracks(self, distance, _y):
        """
        获取轨迹
        """
        tracks = []
        y, v, t, current = 0, 0, 1, 0
        mid = distance * 3 / 4
        exceed = random.randint(40, 90)
        z = random.randint(30, 150)
        while current < (distance + exceed):
            if current < mid /2:
                a = 2
            elif current < mid:
                a = 3
            else:
                a = -3
            a /= 2
            v0 = v
            s = v0 * t + 0.5 * a * (t * t)
            current += int(s)
            v = v0 + a * t
            y += random.randint(-3, -3)
            z = z + random.randint(5, 10)
            tracks.append([min(current, (distance + exceed)), y, z])
        while exceed > 0:
            exceed -= random.randint(0, 5)
            y += random.randint(-3, 3)
            z = z + random.randint(5, 9)
            tracks.append([min(current, (distance + exceed)), y, z])
        tr = []
        for i, x in range(len(tracks)):
            tr.append({
                "x": x[0],
                "y": _y,
                'relative_time': x[2]
            })
        return tr

    def get_detail(self):
        def get_fp():
            with open('dyslider.js', 'r', encoding='utf-8') as f:
                js_code = f.read()





if __name__ == '__main__':
    pass
