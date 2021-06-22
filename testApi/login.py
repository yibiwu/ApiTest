import requests
import pprint
from common.ApiConfig import HandleUrl


class Login:
    def __init__(self, s):
        self.s = s
    def login(self,inData,mode=True):
        url=HandleUrl().conn_url('/api/v2/server/uc/ucenter/login2')
        token = ""
        headers = {
            "Content-Type": "application/json",
            "token": token
        }
        resp=self.s.post(url,headers=headers,json=inData)
        if mode:#获取token
            headers["token"] = resp.json()["data"]["token"]
            self.s.headers.update(headers)
            # return resp.json()["data"]["token"]

        else:#返回响应数据
            return resp.json()



# if __name__ == '__main__':
#     resp=Login().login({'account': 'danwei1', 'password': 'aa123456', 'verifyCode': '', 'client': 'www'})
#     pprint.pprint(resp)