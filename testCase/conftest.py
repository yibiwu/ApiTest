import pytest, requests
from common.Readyaml import YamlUtil

from testApi.login import Login



@pytest.fixture(scope="session")
def login_fixture():
    print('---开始---')
    ss = requests.session()
    s=Login(ss)
    s.login(url='/api/v2/server/uc/ucenter/login2',method='post',inData={'account': 'danwei1', 'password': 'aa123456', 'verifyCode': '', 'client': 'www'})
    yield ss
    print('---结束---')

@pytest.fixture(scope="session",autouse=True)
def clear_yaml():
    YamlUtil().clear_yaml()

