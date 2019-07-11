# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/7/11 19:36
# @Author   : tangky
# @Site     : 
# @File     : config.py
# @Software : PyCharm

import configparser
import os


def getConfig(section, key):
    config = configparser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/settings.conf'
    config.read(path)
    return config.get(section, key)
