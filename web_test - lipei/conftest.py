# -*- coding: utf-8 -*-
"""
    Create Time: 2019/9/6 14:12
    Author: 作者
"""
import pytest
from selenium import webdriver


from pages.login_page import LoginPage



@pytest.fixture()
def init_web():
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    loginpage = LoginPage(browser)
    yield browser,loginpage
    browser.quit()

# @pytest.fixture()
# def login_init_web(init_web):
#     browser, loginpage = init_web
#     yield browser,loginpage
    # loginpage.user_element.clear()
    # loginpage.pwd_element.clear()


# @pytest.fixture()
# def login_success():
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(20)
#     loginpage = LoginPage(browser).login(user_info_success[0],user_info_success[1])
#     yield