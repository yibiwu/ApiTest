import base64
import json

import requests
from common.ReadConfig import ReadConfig
import hashlib
import rsa
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA



class Base:
    def __init__(self,ss):
        self.s=ss

    def conn_url(self, url):
        baseurl = ReadConfig().get_url("url")
        self.url=baseurl+url
        return  self.url

    def send_request(self,method,url,data,**kwargs):
        method=str(method).lower()
        self.url=self.conn_url(url)
        # resp=None
        if method=='get':
            resp=self.s.request(method, self.url,data=data,**kwargs)
        else:
            data=json.dumps(data)
            resp = self.s.request(method, self.url, data=data, **kwargs)
        return resp.json()

    def update_request(self,headers):
        self.s.headers.update(headers)

    def get_md5(self,psw):
        '''
        :param psw:
        :return: 返回md5加密后的值
        '''
        md5=hashlib.md5()
        md5.update(psw.encode("utf-8"))
        return md5.hexdigest()  #16进制

    def create_keys(self):  # 生成公钥和私钥
        (pubkey, privkey) = rsa.newkeys(1024)#创建公钥和私钥，1024为设定你加密字符串的最大可支持加密长度为1024位 = 128字节，你也可以按需设置任意长度，越长加密越慢，越短越快
        # 将公钥和私钥以pem编码格式保存
        pub = pubkey.save_pkcs1()
        #将公钥保存到文件, 将字节写入文件需要加上decode（'utf-8'）
        with open('public.pem', 'wb+')as f: # public.pem，保存的文件名，可更改路径，这里保存在当前路径下
            f.write(pub)
        pri = privkey.save_pkcs1()
        with open('private.pem', 'wb+')as f: # private.pem，保存的文件名，可更改路径，这里保存在当前路径下
            f.write(pri)
        print(f"公钥初始的值为：{pubkey}，以pem格式的保存后的数据为：{pub}")
        print(f"私钥初始的值为：{privkey} \n 以pem格式的保存后的私钥数据为：{pri}")

    def encrypt(self,message):  # 用公钥加密
        with open('public.pem', 'rb') as publickfile:
            p = publickfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(p)
        crypt_text = rsa.encrypt(message, pubkey)
        print(crypt_text)
        return crypt_text  # 加密后的密文

    def decrypt(self,crypt_text):  # 用私钥解密
        with open('private.pem', 'rb') as privatefile:
            p = privatefile.read()
        privkey = rsa.PrivateKey.load_pkcs1(p)
        lase_text = rsa.decrypt(crypt_text, privkey).decode()  # 注意，这里如果结果是bytes类型，就需要进行decode()转化为str
        print(lase_text)
        return lase_text

    def signature(self, message):#签名
        with open('private.pem') as f:
             s = f.read()
        prikey = rsa.PrivateKey.load_pkcs1(s)
        rsakey = RSA.importKey(prikey)
        signer = PKCS1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message.encode())
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
        print(signature)
        return signature


    def verify_sign(self,signature,message):
        with open('master-public.pem') as f:
            key = f.read()
        rsakey = RSA.importKey(key)
        verifier = PKCS1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message.encode())
        is_verify = verifier.verify(digest, base64.b64decode(signature))
        print(is_verify)

if __name__ == '__main__':
    re=Base().get_md5("123456")
    print(re)
    Base().create_keys()
    string='你好'
    crypt_text = Base().encrypt(string.encode('utf-8'))# 使用公钥去加密字符串
    # signature=Base().signature(crypt_text)
    # Base().verify_sign(signature,crypt_text)
    lase_text = Base().decrypt(crypt_text)

