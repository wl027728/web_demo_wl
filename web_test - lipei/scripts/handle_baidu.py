# -*- coding: utf-8 -*-
"""
    Create Time: 2019/8/30 9:05
    Author: 作者
"""
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By

from scripts.constants import LOG_IMG_DIR
from scripts.handle_logging import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# def get_baidu():
#     browser = webdriver.Chrome()
#     browser.get('http://120.78.128.25:8765/Index/login.html')
#     # user_element=browser.find_element_by_name('phones')
#     user_element =WebDriverWait(browser,20).until(EC.presence_of_element_located((By.NAME,'phones')))
#     str = user_element.get_attribute('placeholder')
#     str = str[:-1]
#     print(str)
#     print(type(str))
#
#
#
# if __name__=='__main__':
#     get_baidu()
a='dsfdfdg'
print(a[0:3])