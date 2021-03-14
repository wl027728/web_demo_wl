# -*- coding: utf-8 -*-
"""
    Create Time: 2020/6/24 10:04
    Author: 作者
"""
import time

import pytest
import unittest
import allure

from selenium import webdriver

from data.lian_data import lian_data
from pages.login_page import LoginPage
from pages.BAregister_page import BaoAPage
from  pages.home_page import HomePage
from pages.lian_page import LiAnPage

#browser = webdriver.Chrome()
@pytest.mark.lian
class TestLiAn():
    @pytest.mark.parametrize('lian_inform',lian_data)
    def test_lian01(self,lian_inform,init_web):
        browser,loginpage = init_web
        loginpage.login(lian_inform[0],lian_inform[1])
        # BaoAPage(browser).counterreport(lian_inform[2])
        # BaoAPage(browser).casedispatch()
        # #loginpage.logout()
        # loginpage.login(lian_inform[3],lian_inform[1])
        # LiAnPage(browser).enter_LApage()
        # LiAnPage(browser).input_BDlossinfo()
        # LiAnPage(browser).input_LPcostinfo()
        # LiAnPage(browser).commit_lian()


if __name__ == '__main__':
    unittest.main()