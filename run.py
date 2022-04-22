import os
import sys
curPath=os.path.abspath(os.path.dirname(__file__))
rootPath=os.path.split(curPath)[0]
sys.path.append(rootPath)

import pytest

if __name__ == '__main__':
    pytest.main(['./testCase/test_login.py','-s','--alluredir','./report/tmp','--clean-alluredir'])# -s 打印输出
    os.system('allure generate ./report/tmp -o ./report/html --clean')
    os.system('allure serve  ./report/tmp')