#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import unittest
from selenium import webdriver
import time
import myLogintoout
from selenium.webdriver.common.by import By
class Maker(unittest.TestCase):
    def setUp(self):
        #登录
        self.dr=myLogintoout.getDr("http://localhost:6060/aeaihr/index?Login")
        myLogintoout.mylogin(self.dr)
        time.sleep(2)
        #点击人力资源

        # 定位考勤信息元素

        # 点击元素
        myLogintoout.clickButton(e)
        time.sleep(2)
        #回到大的html
        myLogintoout.toMainHtml(self.dr)

    #签到
    def test_01(self):
        #切入main的html
        myLogintoout.toHtml(self.dr,'mainFrame')
        #获取签到按键元素
        #点击元素
        myLogintoout.clickButton(e)
        time.sleep(2)
        #切换到签到信息页面

        #获取签到输入框元素
        #输入信息

        #获取确认按键元素
        #点击确认按键

        #断言是签到失效（不可用）





    #签退功能（先有签到）
    def test_02(self):
        # 切入main的html
        myLogintoout.toHtml(self.dr, 'mainFrame')
        # 获取签到按键元素
        # 点击元素
        myLogintoout.clickButton(e)
        time.sleep(2)

        # 获取签到输入框元素
        # 输入信息

        # 获取确认按键元素
        # 点击确认按键

        #获取签退按键
        #点击签退按键

        #切换到签退信息框

        #获取签退地址输入框
        #输入信息

        #断言是列表中签退有信息


    #浏览考勤信息
    def test_03(self):
        # 切入main的html
        myLogintoout.toHtml(self.dr, 'mainFrame')
        #获取上一天按键元素
        #点击元素

        #断言是签到和签退按键失效

        #获取下一天按键元素
        #点击元素

        # 获取下一天按键元素
        # 点击元素

        #断言是签到和签退按键失效




    def tearDown(self):
        myLogintoout.toMainHtml(self.dr)
        time.sleep(3)
        myLogintoout.myout(self.dr)
        time.sleep(3)
        self.dr.quit()

if __name__=='__main__':
    unittest.main()