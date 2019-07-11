# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/7/12 6:57
# @Author   : tangky
# @Site     : 
# @File     : appauto_testcase3.py
# @Software : PyCharm

# import os
# import time
# import unittest
# from selenium import webdriver
#
# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
# global driver
#
#
# class Login(unittest.TestCase):
#     def setUp(self) -> None:
#         desired_caps = {}
#         desired_caps['device'] = 'android'
#         desired_caps['platformName'] = 'Android'
#         desired_caps['browserName'] = ''
#         desired_caps['version'] = '4.4'
#         desired_caps['deviceName'] = 'emulator-5554'
#         desired_caps['app'] = PATH('csdn.apk')
#         self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#
#     def test_login(self):
#         time.sleep(10)
#         time.sleep(10)
#         indentity = self.driver.find_element_by_name('输入CSDN账号').send_keys('test')
#         usn = self.driver.find_element_by_name('输入密码')
#         usn.click()
#         usn.send_keys('test2')
#         self.driver.find_element_by_name('登录').click()
#         time.sleep(10)
#
#     def tearDown(self) -> None:
#         self.driver.quit()
#
#
# if __name__ == '__main__':
#     unittest.main()

import time
import os
import unittest


from appium import webdriver


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
global dirver
