# -*- coding: utf-8 -*-
# @File   :douyin_room_ws.py
# @Time   :2024/12/17 14:59
# @Author :admin

import subprocess
from functools import partial
from idlelib.iomenu import encoding

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
import websocket
import json

def get_sign(room_id):
    with open('jsCode_dy_get_sign.js', 'r', encoding='utf-8') as f:
        js_code = f.read()
        sign = execjs.compile(js_code).call('get_sign', room_id)
        return sign


def on_message(ws, message):
    print(message)
    data = json.loads(message)
    print(f"INIFO：{data['text']}")


def on_error(ws, error):
    print(f'错误：{error}')


def on_close(ws):
    print("WebSocket closed")


def on_open(ws):
    ws.send("Hello, Server!")
    

def get_ttwid():
    return ""

def run(room_id="7449246850521090857"):
    sign = get_sign(room_id)
    # ws_url = f"wss://webcast5-ws-web-hl.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.14-beta.0&update_version_code=1.0.14-beta.0&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0%20(Windows%20NT%2010.0;%20Win64;%20x64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/130.0.0.0%20Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&cursor=u-1_h-7449264750226412582_t-1734417279963_r-1_d-1&internal_ext=internal_src:dim|wss_push_room_id:{room_id}|wss_push_did:7408800027164902938|first_req_ms:1734417279841|fetch_time:1734417279963|seq:1|wss_info:0-1734417279963-0-0|wrds_v:7449265486627345647&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7408800027164902938&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&insert_task_id=&live_reason=&room_id={room_id}&heartbeatDuration=0&signature=6/NlL6gbXklc8RHc"
    ws_url = f"wss://webcast5-ws-web-hl.douyin.com/webcast/im/push/v2/?app_name=douyin_web&version_code=180800&webcast_sdk_version=1.0.14-beta.0&update_version_code=1.0.14-beta.0&compress=gzip&device_platform=web&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36&browser_online=true&tz_name=Asia/Shanghai&cursor=h-7449281273526621203_t-1734421053584_r-1_d-1_u-1&internal_ext=internal_src:dim|wss_push_room_id:{room_id}|wss_push_did:7408800027164902938|first_req_ms:1734421053474|fetch_time:1734421053584|seq:1|wss_info:0-1734421053584-0-0|wrds_v:7449281695833921780&host=https://live.douyin.com&aid=6383&live_id=1&did_rule=3&endpoint=live_pc&support_wrds=1&user_unique_id=7408800027164902938&im_path=/webcast/im/fetch/&identity=audience&need_persist_msg_count=15&insert_task_id=&live_reason=&room_id={room_id}&heartbeatDuration=0&signature={sign}"

    headers = {
        'Upgrade': 'websocket',
        'Origin': 'https://live.douyin.com',
        'Cache-Control': 'no-cache',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Pragma': 'no-cache',
        'Connection': 'Upgrade',
        'Sec-WebSocket-Key': 'yNpaIuGDUrDNUmHi5DidGg==',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'Sec-WebSocket-Version': '13',
        'Sec-WebSocket-Extensions': 'permessage-deflate; client_max_window_bits',
    }
    ws = websocket.WebSocketApp(ws_url, header=headers,
                                on_message=on_message,
                                on_error=on_error,
                                )
    ws.on_open
    ws.run_forever()

if __name__ == '__main__':
    room_id = "7449246850521090857"
    room_id = "7448802759111084850"
    room_id = "907898335351"
    run(room_id)
