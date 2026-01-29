# -*- coding: utf-8 -*-
# @File   :unfreezen_broadcast.py
# @Time   :2025/1/3 23:19
# @Author :admin


import requests

def run(live_id=100514):
    url = f'http://newdmy.com:9091/broadcast/unfeeze/{live_id}/'
    res = requests.get(url, verify=False)
    print(f'{live_id} {res.text}')

def main():
    for i in range(100514, 100606):
        run(live_id=i)
if __name__ == '__main__':
    main()

