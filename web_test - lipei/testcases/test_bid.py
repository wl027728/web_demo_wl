# -*- coding: utf-8 -*-
"""
    Create Time: 2019/8/30 14:27
    Author: 作者
"""
# -*- coding: utf-8 -*-

from decimal import Decimal

import pytest
from selenium import webdriver
from data.login_data import user_info_success
from pages.home_page import HomePage
from pages.login_page import LoginPage
from data.xinbao_data import xbchoice_data
import unittest


@pytest.mark.xinbao
class TestXinBao():

    @pytest.mark.parametrize('bid_info',xbchoice_data)
    def test_bid_pop_error(self,bid_info,init_web,):
        browser,loginpage = init_web
        loginpage.login('8000135188','000000')
        HomePage(browser).input_xbmessage(bid_info[0],bid_info[1])
    # @pytest.mark.parametrize('bid_info',bid_button_error)
    # def test_bid_button_error(self, bid_info,init_web):
    #     browser, loginpage = init_web
    #     loginpage.login('18684720553','python')
    #     HomePage(browser).get()
    #     HomePage(browser).bid_elemnt.click()
    #     BidPage(browser).bid_input_element.send_keys(bid_info[0])
    #     error_msg_element = BidPage(browser).get_fail_result()
    #     assert (error_msg_element.text==bid_info[1])
    #
    # @pytest.mark.parametrize('bid_info',bid_success)
    # def test_bid_sucess(self,bid_info,init_web):
    #     browser, loginpage = init_web
    #     loginpage.login('18684720553','python')
    #     HomePage(browser).get()
    #     HomePage(browser).bid_elemnt.click()
    #     before_bid_money = BidPage(browser).get_money_before()
    #     BidPage(browser).bid_input_element.send_keys(bid_info[0])
    #     BidPage(browser).bid_button_element.click()
    #     success_msg_element = BidPage(browser).get_success_result()
    #     assert (success_msg_element.text==bid_info[1])
    #     #通过金额断言投标成功
    #     BidPage(browser).bid_active_element.click()
    #     after_bid_money = UserPage(browser).get_money_after()
    #     assert ((Decimal(before_bid_money)-Decimal('100'))==Decimal(after_bid_money))

if __name__=='__main__':
    unittest.main()