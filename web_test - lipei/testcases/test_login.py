# -*- coding: utf-8 -*-
"""
    Create Time: 2019/8/23 9:01
    Author: 作者
"""
import pytest
import unittest
import allure

from selenium import webdriver

from data.login_data import user_info_error,user_info_invalidate,user_info_success
from pages.login_page import LoginPage

# @allure.feature('登陆模块')
# @pytest.mark.login
# class TestLogin():
#     @allure.story('帐号或密码为空')
#     @pytest.mark.parametrize('user_info',user_info_error)
#     def test_login_01_error(self,user_info,login_init_web):
#         '''
#         帐号或者密码为空
#         :param user_info:
#         :param login_init_web:
#         :return:
#         '''
#         browser,loginpage = login_init_web
#         loginpage.login(user_info[0],user_info[1])
#         error_mg_element = loginpage.get_actual_result()
#         assert (error_mg_element.text==user_info[2])
#     @allure.story('未认证帐号登陆')
#     @pytest.mark.parametrize('user_info',user_info_invalidate)
#     def test_login_02_error(self, user_info,login_init_web):
#         browser,loginpage = login_init_web
#         loginpage.login(user_info[0], user_info[1])
#         invalidate_mg_element = loginpage.get_invalidate_result()
#         assert (invalidate_mg_element.text==user_info[2])
#     @allure.story('登陆成功')
#     @pytest.mark.parametrize('user_info',user_info_success)
#     def test_login_success(self,user_info,login_init_web):
#         browser,loginpage= login_init_web
#         loginpage.login(user_info[0], user_info[1])
#         success_mg_element =HomePage(browser).get_success_result()
#         assert (success_mg_element.text==user_info[2])

# if __name__ == '__main__':
#     unittest.main()
