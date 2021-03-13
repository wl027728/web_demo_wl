# -*- coding: utf-8 -*-
"""
    Create Time: 2019/8/23 9:01
    Author: 作者
"""
import pytest
import unittest
import allure

from selenium import webdriver

from data.bill_change_info_data import bill_change_data
from pages.change_bill_page import Bill_Change_Page
from pages.login_page import LoginPage

@pytest.mark.changebill
class TestBillChange():
    @pytest.mark.parametrize('bill_info',bill_change_data)
    def test_login_01_error(self,bill_info,init_web):
        browser,loginpage = init_web
        loginpage.login(bill_info[0],bill_info[1])
        Bill_Change_Page(browser).change_bill_info(bill_info[2],bill_info[3])

if __name__ == '__main__':
    unittest.main()
