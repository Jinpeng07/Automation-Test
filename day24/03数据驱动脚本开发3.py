#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import time
import pymysql
dr=webdriver.Firefox()
dr.get("https://mail.163.com/register/index.htm?from=163mail#/normal")
time.sleep(2)
e=dr.find_element_by_id('username')

db=pymysql.connect(host='127.0.0.1',port=3306,user="root",passwd='123456',db="mytest202305",charset='utf8')
#创建游标
cur=db.cursor()
cur.execute("select name from user")
#获取查询的结果
data=cur.fetchall()
print(data)
for i in data:
    print(i[0])
    e.send_keys(i[0])
    time.sleep(2)
    e.clear()



time.sleep(3)
dr.quit()


