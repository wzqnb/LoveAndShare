# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 10:49
# @Author  : wenzhaoqing

import json
import requests


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【文兆庆的生鲜超市】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":
    yun_pian = YunPian("ba789d57af5b55d7564dc82279463bc6")

    c=yun_pian.send_sms("2017", "17346932641")
    print(c)
