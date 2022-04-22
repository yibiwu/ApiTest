import allure
from common.Readyaml import YamlUtil

from testApi.req_request import Req_request

@allure.feature('项目申报模块')
class TestRequest():
    @allure.story('项目申报案例')
    def test_001(self,login_fixture):
        with allure.step("step1：登录"):
            res1 = Req_request(login_fixture)
        for i in range(1,3):
            with allure.step("step2：获取申报书ID"):
                res1.sys_util_getId()
                requestId = YamlUtil().read_yaml('requestId')
            with allure.step("step3：添加申报书"):
                res1.req_request_add(requestId,i)
            with allure.step("step4：保存申报书"):
                res1.req_request_formData_save(requestId)
            with allure.step("step5：添加提交申报书"):
                res1.req_request_submit(requestId)
            with allure.step("step6：撤回申报书"):
                res1.req_request_retract(requestId)
            with allure.step("step7：删除申报书"):
                res1.req_request_delete(requestId)
