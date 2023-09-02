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

        # 定位出差信息元素

        # 点击元素
        myLogintoout.clickButton(e)
        time.sleep(2)
        #回到大的html
        myLogintoout.toMainHtml(self.dr)

    #基础信息
    def test_01(self):
        #切入main的html
        myLogintoout.toHtml(self.dr,'mainFrame')
        #获取新增按键元素
        #点击元素
        myLogintoout.clickButton(e)
        time.sleep(2)
        #切换到基础信息页面

        #获取报销时间输入框元素
        #输入信息

        #获取开始时间输入框元素
        #输入信息

        # 获取结束时间输入框元素
        # 输入信息

        # 获取出差天数输入框元素
        # 输入信息

        # 获取补助金额输入框元素
        # 输入信息

        # 获取出差事由输入框元素
        # 输入信息

        #点击保存按键
        获取保存按键
        #
        #断言就是出现费用清单





    #费用清单（先有基础信息）
    def test_02(self):
        # 切入main的html
        myLogintoout.toHtml(self.dr, 'mainFrame')
        # 获取新增按键元素
        # 点击元素
        myLogintoout.clickButton(e)
        time.sleep(2)
        # 切换到基础信息页面

        # 获取报销时间输入框元素
        # 输入信息

        # 获取开始时间输入框元素
        # 输入信息

        # 获取结束时间输入框元素
        # 输入信息

        # 获取出差天数输入框元素
        # 输入信息

        # 获取补助金额输入框元素
        # 输入信息

        # 获取出差事由输入框元素
        # 输入信息

        # 获取保存按键
        # 点击保存按键

        #获取费用清单按键
        #点击该按键

        #切换到费用清单页面

        # 获取出发地输入框元素
        # 输入信息

        # 获取目的地输入框元素
        # 输入信息

        # 获取出发时间选择器元素
        # 选择时间

        # 获取到达时间选择器元素
        # 选择时间

        #获取交通方式选择列表
        #选择交通方式

        # 获取交通费用输入框元素
        # 输入信息

        # 获取住宿费用输入框元素
        # 输入信息

        # 获取其他费用输入框元素
        # 输入信息

        #获取保存按键
        #点击保存按键

        #断言是回到基础信用页面，看汇总费用





    def tearDown(self):
        myLogintoout.toMainHtml(self.dr)
        time.sleep(3)
        myLogintoout.myout(self.dr)
        time.sleep(3)
        self.dr.quit()

if __name__=='__main__':
    unittest.main()