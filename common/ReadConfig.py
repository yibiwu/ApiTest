import configparser
import os

class ReadConfig:
    def __init__(self, filepath=None):
        if filepath:
            configpath = filepath
        else:
            root_dir = os.path.realpath('E:\python\project\ApiTest\common')
            configpath = os.path.join(root_dir, "config.ini")

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def get_db(self, param):
        value = self.cf.get("Mysql", param)
        return value

    def get_url(self, param):
        value = self.cf.get("Url", param)
        return value

if __name__ == '__main__':
    test = ReadConfig()
    t = test.get_url("gdurl")
    t1=test.get_db("host")
    print(t,t1)