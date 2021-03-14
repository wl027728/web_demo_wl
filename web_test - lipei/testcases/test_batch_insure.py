# # -*- coding: utf-8 -*-
# """
#     Create Time: 2020/4/11 19:06
#     Author: 作者
# """
# # -*- coding: utf-8 -*-
# from data.batch_insure_data import batch_data
#
# """
#     Create Time: 2019/8/23 9:01
#     Author: 作者
# """
# import pytest
# import unittest
#
# from selenium import webdriver
#
# from data.login_data import user_info_error,user_info_invalidate,user_info_success
# from pages.login_page import LoginPage
# from data.batch_insure_data import batch_data
# from pages.home_page import HomePage
# from pages.batch_insure_page import BatchInsure
# from pages.get_tasknum import GetTasknum
# from pages.hebao_page import HebaoPage
#
# # @allure.feature('登陆模块')
# #@pytest.mark.login
# class TestLogin():
#     #@allure.story('帐号或密码为空')
#     @pytest.mark.parametrize('batch_data',batch_data)
#     def test_batch_insure_01(self,batch_data,init_web):
#         browser, loginpage = init_web
#         loginpage.login(batch_data[0],batch_data[1])
#         HomePage(browser).batch_insure()
#         BatchInsure(browser).batch_insure_handle(batch_data[2],batch_data[3],batch_data[4],batch_data[5],batch_data[6])
#         #GetTasknum(browser).get_policynum()
#         HebaoPage(browser).hebao(batch_data[7],batch_data[8],batch_data[1])
#
#
#
# if __name__ == '__main__':
#     unittest.main()
