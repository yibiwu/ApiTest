from common.ReadConfig import ReadConfig
import hashlib

class HandleUrl:
    def __init__(self):
        self.data = ReadConfig()
    def conn_url(self,api):
        baseurl = self.data.get_url("url")
        self.url=baseurl+api
        return  self.url

    def get_md5(self,psw):
        '''
        :param psw:
        :return: 返回md5加密后的值
        '''
        md5=hashlib.md5()
        md5.update(psw.encode("utf-8"))
        return md5.hexdigest()  #16进制


if __name__ == '__main__':
    re=HandleUrl().get_md5("123456")
    print(re)
