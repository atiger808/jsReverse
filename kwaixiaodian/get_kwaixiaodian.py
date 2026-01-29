# -*- coding: utf-8 -*-
# @File   :get_kwaixiaodian.py
# @Time   :2025/1/2 11:37
# @Author :admin

import json
import os
import time
from pprint import pprint
import pandas as pd
import time
import random

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = json.load(f)
        print('success')
    return content
def save_json(dic, file_path='data.json'):
    with open(file_path, 'w', encoding='utf-8') as f:
        content = json.dumps(dic)
        f.write(content)
        print('success')

def append_save_json(dic, file_path='快手小店-data.json'):
    with open(file_path, 'a', encoding='utf-8') as f:
        content = json.dumps(dic) + '\n'
        f.write(content)
        print('success')

def get_data(memberId, itemType=1, startDate='2024-09-30', endDate='2024-09-30', PAGE_NUM=1, PAGE_SIZE=200):
    """
    itemType: 1:自建商品，2:快分销
    """
    import requests

    cookies = {
        '_did': 'web_33247591468B83E4',
        'did': 'web_61ekdsql0v51orfp1zou03g6zjvhg1d1',
        'sid': 'kuaishou.shop.b',
        'bUserId': '1000009598213',
        'userId': '3624475766',
        'kuaishou.shop.b_st': 'ChJrdWFpc2hvdS5zaG9wLmIuc3QSoAFRMBYXBUbGvl9RhfW8cLqRzaY9QMBTtuRBqpobvAzAbtUS4gNa7aiqgE-1KwGwUxcoL1gvWwaVkUVAHDPnahfIS8pv2WJ5CdqsL7wPKh4REooPnOD3fTg-3r8EBHEe7YhD9Po4HjM28MoGiF1ZA8JnmvtoayXHI0ksWDGrEfuUkOLoJB8QAScDwurgCKYrzz1YJhzJLHPlVuvFa1mBNJqBGhJOMw2bA-izRy5fvyc0gd4AwUQiIIIrurAXugMnShggvQXwH_x3mtW-tFlphbKQzJoHcopyKAUwAQ',
        'kuaishou.shop.b_ph': 'e7acccb37ef31ab7957686f06ed7f86c9bb9',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '_did=web_33247591468B83E4; did=web_61ekdsql0v51orfp1zou03g6zjvhg1d1; sid=kuaishou.shop.b; bUserId=1000009598213; userId=3624475766; kuaishou.shop.b_st=ChJrdWFpc2hvdS5zaG9wLmIuc3QSoAFRMBYXBUbGvl9RhfW8cLqRzaY9QMBTtuRBqpobvAzAbtUS4gNa7aiqgE-1KwGwUxcoL1gvWwaVkUVAHDPnahfIS8pv2WJ5CdqsL7wPKh4REooPnOD3fTg-3r8EBHEe7YhD9Po4HjM28MoGiF1ZA8JnmvtoayXHI0ksWDGrEfuUkOLoJB8QAScDwurgCKYrzz1YJhzJLHPlVuvFa1mBNJqBGhJOMw2bA-izRy5fvyc0gd4AwUQiIIIrurAXugMnShggvQXwH_x3mtW-tFlphbKQzJoHcopyKAUwAQ; kuaishou.shop.b_ph=e7acccb37ef31ab7957686f06ed7f86c9bb9',
        'kpf': 'PC_WEB',
        'kpn': '',
        'ktrace-str': '1|MS43MDgyNzk3ODg0Njk3ODY4LjM1NDMzODI3LjE3MzU3OTAyMzU5MzYuMTQ4Mw==|MS43MDgyNzk3ODg0Njk3ODY4LjE4Mjk5OTk3LjE3MzU3OTAyMzU5MzYuMTQ4NA==|0|eshop-frontend|plateco|true|src-Js',
        'origin': 'https://kp.kwaixiaodian.com',
        'priority': 'u=1, i',
        'referer': f'https://kp.kwaixiaodian.com/zone-service/member-data-detail/{memberId}',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'memberId': f'{memberId}',
        'queryType': 'MEMBER_ITEM_LIST',
        'dataModelType': 'TABLE_MODEL',
        'ext': {
            'itemType': itemType,
            'PAGE_NUM': PAGE_NUM,
            'PAGE_SIZE': PAGE_SIZE,
        },
        'dateRangeType': 'MONTH',
        'startDate': f'{startDate}',
        'endDate': f'{endDate}',
        'compareStartDate': f'{startDate}',
        'compareEndDate': f'{endDate}',
    }

    response = requests.post(
        'https://kp.kwaixiaodian.com/rest/kp/workbench/org/statistics/fetchMemberData',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"memberId":"2459356640","queryType":"MEMBER_ITEM_LIST","dataModelType":"TABLE_MODEL","ext":{"itemType":1,"PAGE_NUM":1,"PAGE_SIZE":10},"dateRangeType":"MONTH","startDate":"2024-10-01","endDate":"2024-10-31","compareStartDate":"2024-09-01","compareEndDate":"2024-09-30"}'
    # response = requests.post(
    #    'https://kp.kwaixiaodian.com/rest/kp/workbench/org/statistics/fetchMemberData',
    #    cookies=cookies,
    #    headers=headers,
    #    data=data,
    # )
    data = response.json()
    return data


def get_detail(item_id):
    import requests

    cookies = {
        '_did': 'web_33247591468B83E4',
        'did': 'web_61ekdsql0v51orfp1zou03g6zjvhg1d1',
        'sid': 'kuaishou.shop.b',
        'bUserId': '1000009598213',
        'userId': '3624475766',
        'kuaishou.shop.b_st': 'ChJrdWFpc2hvdS5zaG9wLmIuc3QSoAF0kAobw1yVTcGKKVJnGY-2YnbjiIyV8gAw1qiZblwxGhH7x6nTRBibkNCX1dQSktrPaDB9qX7I9NgfKcoXj841cnMJArKEeTLAAMQ6gLsEJGisLN245ToT1vAxIwYYK6f_d3iTWd37OJ5BOUq3KngQXg2cLCjFbZjjcAiNhMHNouxwyDgnJn-kNX_sgE_pJQs6M9b8bQLY7jdrCU1hBjA-GhJx70cBBaGVtEpnSlNxog9ZoqoiIFrqU3DjhMMeuNn1EcOoeYtOeVcc1MggD-S-weGK8KzoKAUwAQ',
        'kuaishou.shop.b_ph': '5cc728d91c7753e14bf5de6e4efd8488a21b',
    }

    # cookies = {
    #     'soft_did': '1619580708547',
    #     'did': 'web_81nbuq0uweydynwz1ff26al45mta9upb',
    #     'bUserId': '1000009598213',
    #     'userId': '3624475766',
    #     'kuaishou.shop.b_st': 'ChJrdWFpc2hvdS5zaG9wLmIuc3QSoAHwMV7u9jFcGzFRjOkUmDy3ZDmHeYyaoM_IJcru1Tn_mb6-PkB9bVLctKzicliicPYMQ5lo29l8-4hJ3o4v2LpZI4CCt-BU4IAFLQrOEykZa1QolQ8I2Inj_cG9OcCwUJkHxe97P6KgfS8r8pKLkgjKqRVMmzCc5BFduvGmzcGtDlvZWD1mhHOzCZYaqIknDrKvU5OLwbWzUxiycfEU7l0eGhIlYdGjF9dJg7vA1C954KBAdRAiIFyHcEtyGz5Qc1lkCPGJs5k7Ropq9qzV30_TexkYF_5PKAUwAQ',
    #     'kuaishou.shop.b_ph': 'aeeca855a54baac0ed39302e2cb45339705b',
    # }


    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/json',
        # 'cookie': '_did=web_33247591468B83E4; did=web_61ekdsql0v51orfp1zou03g6zjvhg1d1; sid=kuaishou.shop.b; bUserId=1000009598213; userId=3624475766; kuaishou.shop.b_st=ChJrdWFpc2hvdS5zaG9wLmIuc3QSoAF0kAobw1yVTcGKKVJnGY-2YnbjiIyV8gAw1qiZblwxGhH7x6nTRBibkNCX1dQSktrPaDB9qX7I9NgfKcoXj841cnMJArKEeTLAAMQ6gLsEJGisLN245ToT1vAxIwYYK6f_d3iTWd37OJ5BOUq3KngQXg2cLCjFbZjjcAiNhMHNouxwyDgnJn-kNX_sgE_pJQs6M9b8bQLY7jdrCU1hBjA-GhJx70cBBaGVtEpnSlNxog9ZoqoiIFrqU3DjhMMeuNn1EcOoeYtOeVcc1MggD-S-weGK8KzoKAUwAQ; kuaishou.shop.b_ph=5cc728d91c7753e14bf5de6e4efd8488a21b',
        # 'cookie':'soft_did=1619580708547; did=web_81nbuq0uweydynwz1ff26al45mta9upb; bUserId=1000009598213; userId=3624475766; kuaishou.shop.b_st=ChJrdWFpc2hvdS5zaG9wLmIuc3QSoAGGAJWL6UF1Y1oMgP7_Y7kqqeVR9bp9LMXAkmf_gMjoqBNhrwaIV7gii2MDDuH5pBJiI6pfJ33_xiq19Xd7rsX0krvcNkHY1bibaUJ4hpqjWtO7eT0zveZhi4et7gmn2nvW3Nl7ggkCbagXzJEAmtiPJjSkFISwPs58YhPke3f2-cmxhHcubWbsjJH6c7ybz-9SAoncQstIuICZ8j81NycnGhLJEp5dRe8bRzILp4WlbdDTnPsiIH2XSmHHevcn6qU_2Ad32NLBb6FMfPP4dzBTbemBczxeKAUwAQ; kuaishou.shop.b_ph=3e55069af420e9032d7e3a7b13074994263b',
        'cookie':'soft_did=1619580708547; did=web_81nbuq0uweydynwz1ff26al45mta9upb; bUserId=1000009598213; userId=3624475766; kuaishou.shop.b_st=ChJrdWFpc2hvdS5zaG9wLmIuc3QSoAGGAJWL6UF1Y1oMgP7_Y7kqqeVR9bp9LMXAkmf_gMjoqBNhrwaIV7gii2MDDuH5pBJiI6pfJ33_xiq19Xd7rsX0krvcNkHY1bibaUJ4hpqjWtO7eT0zveZhi4et7gmn2nvW3Nl7ggkCbagXzJEAmtiPJjSkFISwPs58YhPke3f2-cmxhHcubWbsjJH6c7ybz-9SAoncQstIuICZ8j81NycnGhLJEp5dRe8bRzILp4WlbdDTnPsiIH2XSmHHevcn6qU_2Ad32NLBb6FMfPP4dzBTbemBczxeKAUwAQ; kuaishou.shop.b_ph=3e55069af420e9032d7e3a7b13074994263b',

        'kpf': 'PC_WEB',
        'kpn': 'unknown',
        'ktrace-str': '3|My40NTgzNjk4Mjg2NzM2NzY5LjM5NzIyMzMxLjE3MzU3OTU4NjM5NTcuMTAwMQ==|My40NTgzNjk4Mjg2NzM2NzY5LjM5MTkzMzU3LjE3MzU3OTU4NjM5NTcuMTAwMA==|0|plateco-kfx-service|plateco|true|src:Js,seqn:3880,rsi:68351078-89cf-457f-8245-3209fac4519d,path:/merchant/shop/detail,rpi:343deb66b6',
        'origin': 'https://app.kwaixiaodian.com',
        'priority': 'u=1, i',
        'referer': f'https://app.kwaixiaodian.com/merchant/shop/detail?id={item_id}&hyId=kwaishop&layoutType=4',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    json_data = {
        'sourceType': 'web',
        'id': f'{item_id}',
        'hyId': 'kwaishop',
        'layoutType': '4',
        'itemId': f'{item_id}',
        'cashierParam': '{"installWechat":false,"installAlipay":false,"installWechatSdk":false,"installAlipaySdk":false,"installUnionPaySdk":false,"installUnionPay":false}',
        'fromSource': '',
    }

    response = requests.post(
        'https://app.kwaixiaodian.com/rest/app/kwaishop/product/c/detail/h5/componentized?caver=2&__NS_hxfalcon=HUDR_sFnX-DtsEkFXsbDPT3TMP-sk0is6Segc_xNclq7WsRCxYt9QLz_qrd3MALzfkMhkshbENDI1Bul8CEN_rqrzzbU23pRTmhJ9YA-aV0esm8P3lx6tKbF_LW9rzYhnVnQQWedDJlWDn7yBPwtbiAbETHvN6EJViNxC-bUlhQif$HE_071881e5e7dcbd3269d84d9b6a1b6842f64d4c4c4c4d93d4e0f65ec46ff5866a78a1d84dd71a7296371a72a44c',
        # cookies=cookies,
        headers=headers,
        json=json_data,
    )

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    # data = '{"sourceType":"web","id":"{item_id}","hyId":"kwaishop","layoutType":"4","itemId":'+ str(item_id) + ',"cashierParam":"{\\"installWechat\\":false,\\"installAlipay\\":false,\\"installWechatSdk\\":false,\\"installAlipaySdk\\":false,\\"installUnionPaySdk\\":false,\\"installUnionPay\\":false}","fromSource":""}'
    # response = requests.post(
    #    'https://app.kwaixiaodian.com/rest/app/kwaishop/product/c/detail/h5/componentized?caver=2&__NS_hxfalcon=HUDR_sFnX-DtsEkFXsbDPT3TMP-sk0is6Segc_xNclq7WsRCxYt9QLz_qrd3MALzfkMhkshbENDI1Bul8CEN_rqrzzbU23pRTmhJ9YA-aV0esm8P3lx6tKbF_LW9rzYhnVnQQWedDJlWDn7yBPwtbiAbETHvN6EJViNxC-bUlhQif$HE_071881e5e7dcbd3269d84d9b6a1b6842f64d4c4c4c4d93d4e0f65ec46ff5866a78a1d84dd71a7296371a72a44c',
    #    cookies=cookies,
    #    headers=headers,
    #    data=data,
    # )

    data = response.json()
    return data

def get_process_data(memberId, itemType=1):
    success_list = []
    file_list = [i for i in os.listdir('.') if i.endswith(f'{memberId}.json') and i.startswith('data')]
    item_list = []
    total_num = 0
    for i in file_list:
        data = read_json(i)
        total = data['total']
        total_num += total
        for j in data['data']:
            item_id = j['id']
            if item_id not in item_list:
                item_list.append(item_id)
    print(f'total_num: {total_num}')
    print(f'item_list: {len(item_list)}')


    new_file_path = f'快手小店-data-{itemType}-{memberId}.json'
    if os.path.exists(new_file_path):
        with open(new_file_path, 'r', encoding='utf-8') as f:
            success_list = [json.loads(i)['id'] for i in f.readlines()]

    print(f'success_list: {len(success_list)}')

    old_success_list = []
    old_file_path = f'快手小店-data-1-{memberId}.json'
    if os.path.exists(old_file_path):
        with open(old_file_path, 'r', encoding='utf-8') as f:
            old_success_list = [json.loads(i)['id'] for i in f.readlines()]

    print(f'old_success_list: {len(old_success_list)}')

    real_list = []
    for i in item_list:
        if i not in old_success_list:
            real_list.append(i)

    print(f'real_list: {len(real_list)}')

    exit()


    item_list = real_list
    total_data = []
    n = 0
    for item_id in item_list[:]:
        item = {}

        if item_id not in success_list:
            print(f'item_id: {item_id}')
            print(f'{item_list.index(item_id)}/{len(item_list)}')
            n += 1

            for _ in range(5):
                sep = random.randint(8, 20)
                data = get_detail(item_id)
                print(f'第{_+1}次请求 sleep: {sep}s', data)
                if data.get('result') == 1:
                    dic = data['data']['data']['idDetailShop']['fields']['data']
                    shopName = dic['shopTitle']['shopName']
                    dic['id'] = item_id
                    item['id'] = item_id
                    item['shopName'] = shopName
                    # total_data.append(item)
                    append_save_json(dic, file_path=new_file_path)
                    success_list.append(item_id)
                    time.sleep(sep)
                    break
                time.sleep(sep)


        # if n == 3:
        #     break




    # pd.to_csv('快手小店-data.csv', total_data)


def process_json(memberId, itemType=1):
    with open(f'快手小店-data-{itemType}-{memberId}.json', 'r', encoding='utf-8') as f:
        li = [json.loads(i) for i in f.readlines()]

    total_data = []
    id_list = []
    for dic in li:
        item = {}
        shopName = dic['shopTitle']['shopName']
        item_id = dic['id']
        # item['memberId'] = memberId
        item['id'] = item_id
        item['shopName'] = shopName

        if item_id not in id_list:
            id_list.append(item_id)
            total_data.append(item)
        else:
            print(item_id)
    print(len(id_list), len(total_data))
    df = pd.DataFrame(total_data)
    df.to_csv(f'快手小店-data-{itemType}-{memberId}.csv')


def get_full_data(memberId, itemType=2):
    startDate = '2024-10-01'
    endDate = '2024-10-31'
    PAGE_NUM = 1
    data = get_data(memberId, itemType=itemType, startDate=startDate, endDate=endDate, PAGE_NUM=PAGE_NUM)

    print(data)
    print(len(data['data']))

    file_path = f'data_{startDate}_{endDate}_{itemType}_{memberId}.json'
    save_json(data, file_path)


if __name__ == '__main__':
    # memberId = '2459356640'   # 汉慈医世家
    memberId = '2138479247'   # 嘉龙三叶元跑胡专卖店
    itemType = 1
    get_full_data(memberId, itemType=itemType)
    # get_process_data(memberId, itemType=itemType)
    # process_json(memberId, itemType=itemType)
