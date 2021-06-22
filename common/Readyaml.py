import yaml
def get_yaml_data(fileDir):
    resList=[]#存放响应结果[(请求1,响应1),(请求2,响应2)]
    fir=open(fileDir,'r',encoding="utf-8")
    res =yaml.load(fir,Loader=yaml.FullLoader)
    fir.close()
    info=res[0]
    del res[0]
    for one in res:
        resList.append((one['detail'],one['data'],one['resp']))
    return resList

if __name__ == '__main__':
    res=get_yaml_data('../data/login.yaml')
    print(res)