import json

import requests

from common.ApiConfig import HandleUrl
import pprint


class Req_request():

    def __init__(self, s):
        self.s = s

    def api_post_login(self, account, password, verifyCode, client):
        # headers定义
        token=""
        headers = {
            "Content-Type": "application/json",
            "token":token
        }
        # data定义
        data = {
            "account": account,
            "password": password,
            "verifyCode": verifyCode,
            "client": client
        }
        # 调用post并返回响应对象
        response = self.s.post(HandleUrl().conn_url('/api/v2/server/uc/ucenter/login2'), headers=headers, data=json.dumps(data))
        headers["token"]=response.json()["data"]["token"]
        self.s.headers.update(headers)
        pprint.pprint(response.json())

    def sys_util_getId(self):
        response = self.s.get(HandleUrl().conn_url('/api/v2/server/sys/util/getId'))
        requestId = response.json()["data"]
        print("requestId is "+requestId)
        return requestId


    def req_request_add(self,requestId):
        data={
                "id":requestId,
                "name":"2021520测试1",
                "contactPerson":"1",
                "contactPhone":"1",
                "themeId":"826034192285597696",
                "species":"",
                "falseDeclaration":{
                }
        }
        response=self.s.post(HandleUrl().conn_url('/api/v2/server/req/request/add'),data=json.dumps(data))
        print('添加成功====>')
        print(response.text)
        print('添加成功====>')

    def req_request_formData_save(self, requestId):
        with open("../testApi/formdata.json",'r',encoding='utf-8') as form:
            formdata=json.dumps(json.load(form))
        data={
            "formData":formdata,
            "formHtml":'<div>测试</div>',
            "kind": "request",
            "requestId": requestId
        }
        response=self.s.post(HandleUrl().conn_url('/api/v2/server/req/request/formData/save'),data=json.dumps(data))
        print('保存成功====>')
        print(response.text)
        print('保存成功====>')


    def req_request_submit(self,requestId):
        data={
            "kind": "request",
            "requestId": requestId
        }
        response = self.s.post(HandleUrl().conn_url('/api/v2/server/req/request/submit'),data=json.dumps(data))
        print('提交成功====>')
        print(response.text)
        print('提交成功====>')

    def req_request_retract(self,requestId):
        data={
            "requestId": requestId,
            "remark": "撤回内容",
            "kind": "request"
        }
        response=self.s.post(HandleUrl().conn_url('/api/v2/server/req/request/retract'),data=json.dumps(data))
        print('撤回的项目requestId是'+requestId)
        print(response.text)
        print('撤回成功====>')


    def req_request_delete(self,requestId):
        data={
            "kind": "request",
            "requestId": requestId
        }
        response = self.s.request('post',HandleUrl().conn_url('/api/v2/server/req/request/delete'),data=json.dumps(data))
        print('删除的项目requestId是'+requestId)
        print(response.text)
        print('删除成功====>')



if __name__ == '__main__':  #ctrl+j
    s = requests.session()
    aa = Req_request(s)
    bb = aa.api_post_login('danwei1', 'aa123456', '', 'www')
    cc=aa.sys_util_getId()
    dd=aa.req_request_add(cc)
    ee=aa.req_request_formData_save(cc)
    aa.req_request_submit(cc)
    aa.req_request_retract(cc)
    aa.req_request_delete(cc)



