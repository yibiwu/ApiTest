import allure
import pytest, requests

from testApi.login import Login



@pytest.fixture(scope="session")
def login_fixture():
    ss = requests.session()
    s=Login(ss)
    s.login({'account': 'danwei1', 'password': 'aa123456', 'verifyCode': '', 'client': 'www'})
    yield ss


