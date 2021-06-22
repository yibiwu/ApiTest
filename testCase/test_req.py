import allure
import pytest,os

from testApi.req_request import Req_request

@allure.feature('项目申报模块')
class TestRequest():
    @allure.story('项目申报案例')
    def test_001(self,login_fixture):
        with allure.step("step1：登录"):
            res1 = Req_request(login_fixture)
        with allure.step("step2：获取申报书ID"):
            cc = res1.sys_util_getId()
        with allure.step("step3：添加申报书"):
            res1.req_request_add(cc)
        with allure.step("step4：保存申报书"):
            res1.req_request_formData_save(cc)
        with allure.step("step5：添加提交申报书"):
            res1.req_request_submit(cc)


    # if __name__ == '__main__':
    #     pytest.main(['test_req.py','-s','--alluredir','../report/tmp'])# -s 打印输出
    #     os.system('allure serve  ../report/tmp')