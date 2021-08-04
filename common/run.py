import pytest,os

if __name__ == '__main__':
    pytest.main(['../testCase/test_login.py','-s','--alluredir','../report/tmp','--clean-alluredir'])# -s 打印输出
    os.system('allure serve  ../report/tmp')