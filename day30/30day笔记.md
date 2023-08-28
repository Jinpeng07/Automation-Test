## requests参数化-csv文件-完整版

```
目的:
把csv文件中的中文词汇翻译成英文,写到csv对应的地方

#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import csv
import requests
import hashlib
import time
#把csv文件中的中文词汇翻译成英文,写到csv对应的地方

#读csv
def ReadCsv(filename):
    mylist=[]
    with open(filename, 'r',encoding='utf-8') as f:
        obj = csv.reader(f)
        print(obj)
        for i in obj:
            mylist.append(i)
    return mylist



#写csv
def WriteCsv(filename,mylist):
    with open(filename,'w',encoding='utf8',newline='') as f:
        #需要把f转换为csv对象
        obj=csv.writer(f)
        for i in mylist:
            obj.writerow(i)


#加密函数
def MyMd5(mystr):
    mdmystr=hashlib.md5(mystr.encode(encoding='utf-8')).hexdigest()
    return mdmystr

def test_baidu():
    mylist=ReadCsv("data.csv")
    dismylist=[['中文','英文']]
    for i in mylist:
        if i==['中文','英文']:
            continue
        #url
        url='https://fanyi-api.baidu.com/api/trans/vip/translate'
        mdmystr=MyMd5("20210507000816969"+i[0]+"123456sGZsjo0Y2OThznTznsRT")
        #参数
        data={
            "q":i[0],
            "from":"zh",
            "to":"en",
            "appid":"20210507000816969",
            "salt":"123456",
            "sign":mdmystr
        }
        #20210507000816969test123456sGZsjo0Y2OThznTznsRT
        #请求
        res=requests.get(url,params=data)
        #把响应转换为json格式,便于后面获取里面的内容
        jr=res.json()
        #获取响应后的翻译结果
        rdata=jr['trans_result'][0]['dst']
        tmplist=[i[0],rdata]
        dismylist.append(tmplist)

        time.sleep(2)

    print(dismylist)
    WriteCsv("data.csv",dismylist)

test_baidu()
```



## requests参数化-txt文件

```
目的:把后台程序的接口参数化,意思把接口的数据放到.txt中
#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import requests
import unittest

def mytest():
    mystr='{"code":"200","msg":"成功","data":None}'
    myjson=eval(mystr)
    print(myjson)
    print(type(myjson))

# mytest()

# while True:
#     pass

class Maker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mylist=[]
        with open("data.txt","r",encoding='utf8') as f:
            cls.mylist=f.read().splitlines()
        cls.ip=cls.mylist[0].split(":",1)[1]
        cls.port=cls.mylist[1].split(":")[1]

        cls.route1=cls.mylist[4].split(":")[1]
        cls.route2 = cls.mylist[5].split(":")[1]
        cls.route3 = cls.mylist[6].split(":")[1]
        cls.route4 = cls.mylist[7].split(":")[1]

        cls.ex1=eval(cls.mylist[21].split(":",1)[1])
        cls.ex2 = eval(cls.mylist[22].split(":", 1)[1])
        cls.ex3 = eval(cls.mylist[23].split(":", 1)[1])
        cls.ex4 = eval(cls.mylist[24].split(":", 1)[1])

        cls.way1=cls.mylist[15]
        cls.way2 = cls.mylist[16]
        cls.way3 = cls.mylist[17]
        cls.way4 = cls.mylist[18]




    #首页(ip,port,路径,预期结果,请求方式)
    def test_01(self):
        res=''
        if self.way1=="首页:get":
            res=requests.get(self.ip+":"+self.port+self.route1)
        elif self.way1=="首页:post":
            res = requests.post(self.ip + ":" + self.port + self.route1)
        #预期结果
        myres=self.ex1
        rj=res.json()
        self.assertEqual(myres,rj,'用例未通过')

    #注册(ip,port,路径,预期结果,请求方式,参数)
    def test_02(self):
        data={"name":"maker","passwd":"123456","email":"25224234@qq.com"}
        res=''
        if self.way2=="注册:get":
            res=requests.get(self.ip+":"+self.port+self.route2,params=data)
        elif self.way2=="注册:post":
            res=requests.post(self.ip+":"+self.port+self.route2,params=data)
        # 预期结果
        myres = self.ex2
        rj = res.json()
        self.assertEqual(myres, rj, '用例未通过')

    #登录(ip,port,路径,预期结果,请求方式,参数)
    def test_03(self):
        data = {"name": "maker", "passwd": "123456"}
        res = ''
        if self.way3 == "登录:post":
            res = requests.post(self.ip + ":" + self.port + self.route3, data=data)
        elif self.way3 == "登录:get":
            res = requests.get(self.ip + ":" + self.port + self.route3, data=data)

        # 预期结果
        myres = self.ex3
        rj = res.json()
        self.assertEqual(myres, rj, '用例未通过')

    #个人信息(ip,port,路径,预期结果,请求方式,参数)
    def test_04(self):
        data = {"name": "maker"}
        res=''
        if self.way4=='个人信息:post-json':
            res = requests.post(self.ip+":"+self.port+self.route4, json=data)
        elif self.way4=='个人信息:post':
            res = requests.post(self.ip + ":" + self.port + self.route4, data=data)
        # 预期结果
        myres =self.ex4
        rj = res.json()
        self.assertEqual(myres, rj, '用例未通过')

if __name__=='__main__':
    unittest.main()



```

