import json

import requests

from common.ApiConfig import Base


from common.Readyaml import YamlUtil


class Req_request():

    def __init__(self, ss):
        self.s = Base(ss)

    def api_post_login(self,url,method,inData):
        token = ""
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "Content-Type": "application/json",
            "token": token
        }
        resp=self.s.send_request(method=method,url=url,headers=headers,data=inData)
        headers["token"] = resp["data"]["token"]
        self.s.update_request(headers)
        print(ss.headers)



    def sys_util_getId(self):
        response=self.s.send_request(method='get', url='/api/v2/server/sys/util/getId',data='')
        # requestId = response.json()["data"]
        YamlUtil().write_yaml({'requestId':response["data"]})
        # return requestId


    def req_request_add(self,requestId,i):
        data={
                "id":requestId,
                "name":"自动化测试项目"+str(i),
                "contactPerson":"1",
                "contactPhone":"1",
                "themeId":"726804852398620672",
                "species":"",
                "falseDeclaration":{
                }
        }
        response=self.s.send_request(method='get', url='/api/v2/server/sys/util/getId',data=data)
        print('添加成功====>')
        print(response)
        print('添加成功====>')

    def req_request_formData_save(self, requestId):
        with open("../testApi/formdata.json",'r',encoding='utf-8') as form:
            formdata=json.dumps(json.load(form))
        print(requestId)
        data={
            "formData":formdata,
            "formHtml":'<div>测试</div>',
            "kind": "request",
            "requestId": requestId
        }
        print(json.dumps(data))
        response=self.s.send_request(method='post',url='/api/v2/server/req/request/formData/save',data=data)
        print('保存成功====>')
        print(response)
        print('保存成功====>')


    def req_request_submit(self,requestId):
        data={
            "kind": "request",
            "requestId": requestId
        }
        response = self.s.send_request(method='post',url='/api/v2/server/req/request/submit',data=data)
        print('提交成功====>')
        print(response)
        print('提交成功====>')

    def req_request_retract(self,requestId):
        data={
            "requestId": requestId,
            "remark": "撤回内容",
            "kind": "request"
        }
        response=self.s.send_request(method='post',url='/api/v2/server/req/request/retract',data=data)
        print('撤回的项目requestId是'+requestId)
        print(response)
        print('撤回成功====>')


    def req_request_delete(self,requestId):
        data={
            "kind": "request",
            "requestId": requestId
        }
        response = self.s.send_request(method='post',url='/api/v2/server/req/request/delete',data=data)
        print('删除的项目requestId是'+requestId)
        print(response)
        print('删除成功====>')



if __name__ == '__main__':  #ctrl+j
    ss=requests.session()
    aa = Req_request(ss)
    aa.api_post_login(url='/api/v2/server/uc/ucenter/login2',method='post',inData={'account': 'danwei1', 'password': 'aa123456', 'verifyCode': '', 'client': 'www'})
    aa.sys_util_getId()
    cc=YamlUtil().read_yaml('requestId')
    aa.req_request_add(cc,1)
    print(ss.headers)
    aa.req_request_formData_save(cc)
    aa.req_request_submit(cc)
    aa.req_request_retract(cc)
    aa.req_request_delete(cc)



