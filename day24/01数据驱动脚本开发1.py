#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====


from selenium import webdriver
import time
import mydata

#往QQ邮箱登录页面的用户名输入框输入内容
def mytest():
    dr=webdriver.Firefox()
    dr.get("https://mail.qq.com/")
    time.sleep(3)
    #切换到小的html,小括号中的值是iframe标签的id或name的值
    #获取第一个内层的iframe元素
    e=dr.find_element_by_class_name("QQMailSdkTool_login_loginBox_qq_iframe")
    dr.switch_to.frame(e)

    #切换到第二内层
    dr.switch_to.frame("ptlogin_iframe")
    dr.find_element_by_id('switcher_plogin').click()#点击密码登录
    time.sleep(2)
    e=dr.find_element_by_id('u')#获取输入框
    e.send_keys(mydata.mydict['qq'])
    time.sleep(3)

    e=dr.find_element_by_id('p')
    e.send_keys(mydata.mydict['passwd'])
    time.sleep(3)
    dr.quit()

mytest()