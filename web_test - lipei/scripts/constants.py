# -*- coding: utf-8 -*-
"""
    Create Time: 2019/7/12 14:36
    Author: 作者
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#获取日志截图文件的路径
LOG_IMG_DIR = os.path.join(BASE_DIR,'log_img')

#获取日志文件的路径
LOGS_FILE_PATH = os.path.join(BASE_DIR,'logs')

#获取配置文件的路径
CONFIGS_DIR= os.path.join(BASE_DIR,'configs')
CONFIGS_FILE_PATH= os.path.join(CONFIGS_DIR,'testcase.conf')
ACCOUNT_FILE_PATH = os.path.join(CONFIGS_DIR,'account.conf')

#获取测试数据文件的路径
TEST_DATAS_DIR= os.path.join(BASE_DIR,'datas')


#获取测试报告文件的路径
REPORTS_FILE_DIR = os.path.join(BASE_DIR,'reports')

#获取测试用例文件的路径
TEST_CASES_DIR = os.path.join(BASE_DIR,'cases')
TEST_CASES_PATH= os.path.join(TEST_CASES_DIR,'batchdata.xlsx')
#


