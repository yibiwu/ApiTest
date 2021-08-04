import json

import requests
import pprint
from common.ApiConfig import Base


class Login:
    def __init__(self,ss):
        self.s = Base(ss)

    def login(self,url,method,inData,mode=True):
        token = ""
        headers = {
            "Content-Type": "application/json",
            "token": token
        }
        resp=self.s.send_request(method=method,url=url,headers=headers,data=inData)
        if mode:#获取token
            headers["token"] = resp["data"]["token"]
            self.s.update_request(headers)
            # return resp.json()["data"]["token"]

        else:#返回响应数据
            return resp



# if __name__ == '__main__':
#     ss=requests.session()
#     resp=Login(ss).login(url='/api/v2/server/uc/ucenter/login2',method='post',inData={'account': 'danwei1', 'password': 'aa123456', 'verifyCode': '', 'client': 'www'},mode=True)