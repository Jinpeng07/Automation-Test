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

        # 定位基本信息元素

        # 点击元素
        myLogintoout.clickButton(e)
        time.sleep(2)
        #回到大的html
        myLogintoout.toMainHtml(self.dr)

    #添加员工基本信息
    def test_01(self):
        #切入main的html
        myLogintoout.toHtml(self.dr,'mainFrame')
        #获取新增员工按键元素
        #点击元素
        myLogintoout.clickButton(e)
        time.sleep(2)
        #切换到员工信息页面

        #获取编号输入框元素
        #输入信息

        #获取姓名输入框元素
        # 输入信息

        # 获取部门输入框元素
        # 输入信息

        # 获取岗位输入框元素
        # 输入信息

        #获取保存按键元素
        #点击保存按键

        #断言是出现三个子菜单，分别是学习经历，工作经历，工作调动





    #添加员工学习经历，前提是有基本信息
    def test_02(self):
        # 切入main的html
        myLogintoout.toHtml(self.dr, 'mainFrame')
        # 获取新增员工按键元素
        # 点击元素
        myLogintoout.clickButton(e)
        time.sleep(2)
        # 切换到员工信息页面

        # 获取编号输入框元素
        # 输入信息

        # 获取姓名输入框元素
        # 输入信息

        # 获取部门输入框元素
        # 输入信息

        # 获取岗位输入框元素
        # 输入信息

        # 获取保持按键元素
        # 点击保持按键



        #点击学习经历按键
        # 器
        #选择日期切换到弹出的窗口
        #点击入学日期的日历

        # 点击截止日期的日历器
        # 选择日期

        #填入学习经历信息

        #点击保存按键

        #断言是人力资源负责人的页面可以看到员工的学习经历
        #断言是普通员工也能看到自己的学习经历


    #工作经历
    def test_03(self):
        # 切入main的html
        myLogintoout.toHtml(self.dr, 'mainFrame')
        # 获取新增员工按键元素
        # 点击元素
        myLogintoout.clickButton(e)
        time.sleep(2)
        # 切换到员工信息页面

        # 获取编号输入框元素
        # 输入信息

        # 获取姓名输入框元素
        # 输入信息

        # 获取部门输入框元素
        # 输入信息

        # 获取岗位输入框元素
        # 输入信息

        # 获取保持按键元素
        # 点击保持按键

        # 点击工作经历按键
        # 切换到弹出的窗口
        # 点击开始工作日期的日历器
        # 选择日期

        # 点击截止日期的日历器
        # 选择日期

        # 填入工作经历信息

        # 点击保持按键

        # 断言是人力资源负责人的页面可以看到员工的工作经历
        # 断言是普通员工也能看到自己的工作经历



    def tearDown(self):
        myLogintoout.toMainHtml(self.dr)
        time.sleep(3)
        myLogintoout.myout(self.dr)
        time.sleep(3)
        self.dr.quit()

if __name__=='__main__':
    unittest.main()