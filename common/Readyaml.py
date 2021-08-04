import os

import yaml
class YamlUtil():
    def get_yaml_data(self,fileDir):
        resList=[]#存放响应结果[(请求1,响应1),(请求2,响应2)]
        fir=open(fileDir,'r',encoding="utf-8")
        res =yaml.load(fir,Loader=yaml.FullLoader)
        print(res)
        fir.close()
        info=res[0]
        del res[0]
        for one in res:
            resList.append((info['url'],info['method'],one['detail'],one['data'],one['resp']))
        return resList


    def read_yaml(self,key):
        with open(os.path.abspath(os.path.join(os.getcwd(), ".."))+'/data/extract.yaml','r',encoding="utf-8") as f:
            value=yaml.load(f,Loader=yaml.FullLoader)
            return value[key]

    def write_yaml(self,data):
        with open(os.path.abspath(os.path.join(os.getcwd(), ".."))+'/data/extract.yaml','a',encoding="utf-8") as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    def clear_yaml(self):
        with open(os.path.abspath(os.path.join(os.getcwd(), ".."))+'/data/extract.yaml', 'w', encoding="utf-8") as f:
            f.truncate()


if __name__ == '__main__':
    res=YamlUtil().get_yaml_data('../data/login.yaml')
    print(res)