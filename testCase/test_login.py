import requests

from common.Readyaml import YamlUtil
from testApi.login import Login

#获取用例数据
# res=get_yaml_data('../data/login.yaml')[1]
# print(res)
# #调用接口，获取响应数据
# resp=Login().login(res['data'],False)
# #断言
# if resp["code"] == res['resp']['code']:
#     print("---用例通过---")

'''

'''


import pytest
import allure

@allure.feature('登录模块')
class TestLogin():
    @allure.story('登录案例')
    @pytest.mark.parametrize('url,method,detail,inBody,expData',YamlUtil().get_yaml_data('../data/logincsv.yaml'))#数据驱动方法
    def test_login(self,url,method,detail,inBody,expData):
        allure.dynamic.title(detail)
        res = Login(requests).login(url,method,inBody,False)
        assert res["code"] == expData['code']


    '''
    F  用例失败
    E  ERROR
    .  用例成功
    '''

    '''
    allure报告方案的原理
        1- 生成报告所需的文件
        2-使用一些工具打开可视化报告
    '''
