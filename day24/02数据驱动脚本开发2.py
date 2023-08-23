#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
from selenium import webdriver
import time
import csv

#
dr=webdriver.Firefox()
dr.get("https://mail.163.com/register/index.htm?from=163mail#/normal")
time.sleep(2)
e=dr.find_element_by_id('username')

with open('1.csv','r',encoding='utf8') as f:
    obj=csv.reader(f)
    for i in obj:
        e.send_keys(i[0])
        time.sleep(2)
        e.clear()

time.sleep(3)
dr.quit()


