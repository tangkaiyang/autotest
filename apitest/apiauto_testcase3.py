# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/7/11 7:19
# @Author   : tangky
# @Site     : 
# @File     : apiauto_testcase3.py
# @Software : PyCharm

import requests, time, sys, re
import urllib, zlib
import pymysql
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from time import sleep

HOSTNAME = '127.0.0.1'


def readSQLcase():  # 读取数据库中响应的接口用例数据
    sql = "SELECT `id`, `apiname`, `apiurl`, `apimethod`, `apiparamvalue`, `apiresult`, `apistatus` from apitest_apistep where apitest_apistep.Apitest_id = 3;"
    conn = pymysql.connect(user='root', passwd='root', db='autotest', port=3306, host='127.0.0.1', charset='utf8')
    cursor = conn.cursor()
    aa = cursor.execute(sql)
    info = cursor.fetchmany(aa)
    for ii in info:
        case_list = []
        case_list.append(ii)
        # CredentialId()
        interfaceTest(case_list)
    conn.commit()
    cursor.close()
    conn.close()


def interfaceTest(case_list):
    res_flags = []
    request_urls = []
    responses = []
    strinfo = re.compile('{TaskId}')
    strinfo1 = re.compile('{AssetId}')
    strinfo2 = re.compile('{PointId}')
    assetinfo = re.compile('{assetno}')
    tasknoinfo = re.compile('{taskno}')
    schemainfo = re.compile('{schema}')
    for case in case_list:
        try:
            case_id = case[0]
            interface_name = case[1]
            method = case[3]
            url = case[2]
            param = case[4]
            res_check = case[5]
        except Exception as e:
            return '测试用例格式不正确%s' % e

        if param == '':
            new_url = r'http://api.test.com.cn' + url
        elif param == 'null':
            new_url = r'http://' + url
        else:
            url = strinfo.sub(TaskId, url)
            param = strinfo.sub(TaskId, param)
            param = tasknoinfo.sub('TaskId', param)
            new_url = r'http://127.0.0.1' + url
            request_urls.append(new_url)
        if method.upper() == 'GET':
            headers = {'Authorization': '', 'Content-Type': 'application/json'}
            if '=' in urlParam(param):
                data = None
                print(
                    str(case_id) + ' request is get ' + new_url.encode('utf-8') + '?' + urlParam(param).encode('utf-8'))
                results = requests.get(new_url + '?' + urlParam(param), data, headers=headers).text
                print('response is get' + results.encode('utf-8'))
                responses.append(results)
                res = readRes(results, '')
            else:
                print('request is get' + new_url + 'body is ' + urlParam(param))
                data = None
                req = urllib.request.Request(url=new_url, data=data, headers=headers, method="GET")
                results = urllib.request.urlopen(req).read()
                print('response is get')
                print(results)
                res = readRes(results, res_check)
                # print(results)
            if res == 'pass':
                writeResult(case_id, '1')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, '0')
        if method.upper() == 'PUT':
            headers = {'Host': HOSTNAME, 'Connection': 'keep-alive', 'CredentialId': id,
                       'Content-Type': 'application/json'}
            body_data = param
            results = requests.put(url=url, data=body_data, headers=headers)
            responses.append(results)
            res = readRes(results, res_check)
            if res == 'pass':
                writeResult(case_id, 'pass')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, 'fail')
                writeBug(case_id, interface_name, new_url, results, res_check)

            try:
                preOrderSN(results)
            except:
                print('ok')
        if method.upper() == 'PATCH':
            headers = {'Authorization': 'Credential' + id, 'Content-Type': 'application/json'}
            data = None
            results = requests.patch(new_url + '?' + urlParam(param), data, headers=headers).text
            responses.append(results)
            res = readRes(results, res_check)
            if res == 'pass':
                writeResult(case_id, 'pass')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, 'fail')
                writeBug(case_id, interface_name, new_url, results, res_check)
            try:
                preOrderSN(results)
            except:
                print('ok')
        if method.upper() == 'POST':
            headers = {'Authorization': 'Credential' + id, 'Content-Type': 'application/json'}
            if "=" in urlParam(param):
                data = None
                results = requests.patch(new_url + '?' + urlParam(param), data, headers=headers).text
                print('response is post' + results.encode('utf-8'))
                responses.append(results)
                res = readRes(results, '')
            else:
                print(str(case_id) + 'request is ' + new_url.encode('utf-8') + 'body is ' + urlParam(param).encode(
                    'utf-8'))
                results = requests.post(new_url, data=urlParam(param).encode('utf-8'), headers=headers).text
                print('response is post' + results.encode('utf-8'))
                responses.append(results)
                res = readRes(resultls, res_check)
            if res == 'pass':
                writeResult(case_id, '1')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, '0')
                writeBug(case_id, interface_name, new_url, results, res_check)
            try:
                TaskId(results)
            except:
                print('ok1')


def readRes(res, res_check):
    res = res.decode().replace('":"', "=").replace('":', "=")
    res_check = res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return "错误,返回参数和预期结果不一致" + s
    return 'pass'


def urlParam(param):
    param1 = param.replace('&quot;', '""')
    return param1


def CredentialId():
    global id
    url = r'http://api.test.com.cn/api/Secutrity/Authentication/Signin/web'
    body_data = json.dumps({"Identity": 'test', 'Password': 'test'})
    headers = {'Connection': 'keep-alive', 'Content-Type': 'application/json'}
    response = requests.post(url=url, data=body_data, headers=headers)
    data = response.text
    regx = '.*"CredentialId":"(.*)","Scene"'
    pm = re.search(regx, data)
    id = pm.group(1)
