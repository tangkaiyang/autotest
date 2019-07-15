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
import sys
import re
import urllib
import zlib
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep

import unittest
import requests, pymysql
from appium import webdriver
import HTMLTestRunner

from apitest import config

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
global driver

HOSTNAME = '127.0.0.1'


class Calculator(unittest.TestCase):
    def setUp(self) -> None:
        time.sleep(1)

    def readSQLcase():
        sql = "SELECT `id`,`appcasename`,`appfindmethod`,`appevelement`,`appoptmethod`,`appassertdata`,`apptestresult` from apptest_appcasestep where apptest_appcasestep.Appcase_id=1 ORDER BY `id` ASC"
        conn = pymysql.connect(host=config.getConfig("database", "host"), port=3306, user='root', passwd='root',
                               db='autotest', charset='utf8')
        cursor = conn.cursor()
        aa = cursor.execute(sql)
        info = cursor.fetchmany(aa)
        for ii in info:
            case_list = []
            case_list.append(ii)
            apptestcase(case_list)
        conn.commit()
        cursor.close()
        conn.close()


def apptestcase(case_list):
    for case in case_list:
        try:
            case_id = case[0]
            findmethod = case[2]
            evelement = case[3]
            optmethod = case[4]
        except Exception as e:
            return "测试用例格式不正确! %s" % e
        print(evelement)
        time.sleep(10)
        if optmethod == 'click' and findmethod == 'find_element_by_id':
            driver.find_element_by_id(evelement).send_keys('wayto')
        elif optmethod == 'click' and findmethod == 'find_element_by_name':
            driver.find_element_by_id(evelement).click()
        elif optmethod == 'sendkey':
            driver.find_element_by_name(evelement).send_keys()


def writeResult(case_id, result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = 'UPDATE apptest_appcasestep set apptest_appcasestep.apptestresult=%s,apptest_appcasestep.create_time=%s where apptest_appcasestep.id=%s;'
    param = (result, now, case_id)
    print('app autotest result is' + result.decode())
    conn = pymysql.connect(user='root', passwd='root', db='autotest', port=3306, host='127.0.0.1', charset='utf8')
    cursor = conn.cursor()
    cursor.execute(sql, param)
    conn.commit()
    cursor.close()
    conn.close()


def caseWriteResult(case_id, result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE apptest_appcase set apptest_apptest.apptestresult=%s,apptest_apptest.create_time=%s where apptest_apptest.id=%s;"
    param = (result, now, case_id)
    print('app autotest result is ' + result.decode())
    conn = pymysql.connect(user='root', passwd='root', db='autotest', host='127.0.0.1', port=3306, charset='utf8')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == '__main__':
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.4'
    desired_caps['deviceName'] = 'emulator-5554'
    # desired_caps['appPackage'] = 'com.android.test'
    desired_caps['appPackage'] = 'com.android.Calculator2'
    desired_caps['appAcitvity'] = '.Calculator'
    desired_caps['app'] = PATH('E:\\release\\csdn.apk')

    time.sleep(1)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(1)
    # readSQLcase()
    # driver.quit()
    # print('Done!')
    # time.sleep(1)

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Calculator("test_readSQLcase"))
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), r'templates\apptest_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"app自动化测试汇总报告", description=u"app自动化测试")
    runner.run(testunit)
    driver.quit()
    print('Done!')
    time.sleep(1)
