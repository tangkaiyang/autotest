# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/7/15 7:28
# @Author   : tangky
# @Site     : 
# @File     : webauto_testcase3.py
# @Software : PyCharm

import os
import time

import unittest
import pymysql
from selenium import webdriver
import HTMLTestRunner

from apitest import config

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
global driver
HOSTNAME = '127.0.0.1'


class Search(unittest.TestCase):
    """搜索:自动化测试平台开发, 软件自动化测试开发"""

    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.get(r"http://www.baidu.com")
        time.sleep(1)

    def test_readSQLcase1(self):
        # 流程相关接口
        sql = "SELECT `id`,`webfindmethod`,`webevelement`,`weboptmethod`,`webtestdata`,`webassertdata`,`webtestresult` from webtest_webcasestep where webtest_webcasestep.webcase_id=1 ORDER BY id ASC"
        conn = pymysql.connect(user='root', passwd='root', db='autotest', host=config.getConfig("database", "host"),
                               charset='utf8')
        cursor = conn.cursor()
        aa = cursor.execute(sql)
        info = cursor.fetchmany(aa)
        for ii in info:
            case_list = []
            case_list.append(ii)
            webtestcase(case_list, self)
        conn.commit()
        cursor.close()
        conn.close()

    def tearDown(self) -> None:
        self.driver.quit()


def webtestcase(case_list, self):
    for case in case_list:
        try:
            case_id = case[0]
            findmethod = case[1]
            evelement = case[2]
            optmethod = case[3]
            testdata = case[4]
        except Exception as e:
            return "测试用例格式不正确! %s" % e
        print(case)
        time.sleep(5)
        if optmethod == 'sendkeys' and findmethod == 'find_element_by_id':
            self.driver.find_element_by_id(evelement).send_keys(testdata)
        elif optmethod == 'click' and findmethod == 'find_element_by_name':
            print(evelement)
            self.driver.find_element_by_name(evelement).click()
        elif optmethod == 'click' and findmethod == 'find_element_id':
            print(evelement)
            self.driver.find_element_by_id(evelement).click()


if __name__ == '__main__':
    time.sleep(1)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Search("test_readSQLcase1"))
    testunit.addTest(Search("test_readSQLcase2"))

    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), r'templates\webtest_report.html')
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"web自动化测试报告", description=u"搜索测试用例")
    runner.run(testunit)
    print('Done!')
    time.sleep(1)
