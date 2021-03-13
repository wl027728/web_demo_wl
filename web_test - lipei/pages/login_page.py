# -*- coding: utf-8 -*-
"""
    Create Time: 2019/8/24 14:15
    Author: 作者
"""
import os
import time
import unittest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scripts.constants import LOG_IMG_DIR
from scripts.handle_logging import logger
from selenium.webdriver import ActionChains
from pages.base_page import Element,BasePage


class LoginPage(BasePage):
    url = 'http://10.98.132.17:8082/workbench/index.html'
    user_locator = ('id',"casUsername")
    pwd_locator = (By.ID,'casPassword')
    login_locator = (By.XPATH,'//form[@id="fm"]/div/div[4]/button')
    cbplatform_locator = (By.XPATH,'//div[@id="topMenu"]/nav/a/div/div')
    down_angle_locator = (By.XPATH,"//h5")
    re_login_locator = (By.XPATH,"//a[@onclick='loginOut()']")
    smlink_locator = (By.XPATH,'//h1[text()="您的连接不是私密连接"] ')
    Gaoji_locator = (By.XPATH,'//button[@id="details-button"]')
    continue_visit_locator = (By.XPATH,'//a[@id="proceed-link"]')
    smoking_sign_locator =(By.XPATH,"//p[@class='loTop']/img[2]")
    more_button_loctor = (By.XPATH,'//div[@id="login_tips"]/div/button')
    dadi_sign_locator = (By.XPATH,'//div[@id="container"]/../div[3]/img')
    user_element = Element(user_locator)
    pwd_element = Element(pwd_locator)
    login_element = Element(login_locator)



    def login(self,username,password):
        '''登陆'''
        self.browser.get(self.url)
        self.browser.maximize_window()
        time.sleep(2)
        if self.get_element_num(self.smlink_locator)==1:
            self.get_element(self.Gaoji_locator).click()
        time.sleep(1)
        if self.get_element_num(self.continue_visit_locator)==1:
            self.get_element(self.continue_visit_locator).click()
        self.waite_visible_element(self.dadi_sign_locator)
        time.sleep(1)
        class_name = self.get_element(self.smoking_sign_locator).get_attribute('class')
        if 'block'in class_name:
            self.get_element(self.smoking_sign_locator).click()
        self.waite_visible_element(self.login_locator)
        time.sleep(2)
        self.user_element.send_keys(username)
        self.pwd_element.send_keys(password)
        self.login_element.click()

        time.sleep(2)

    def logout(self):
        self.switch_window_by_title('财意理赔')
        ActionChains(self.browser).move_to_element(self.get_element(self.down_angle_locator)).perform()
        time.sleep(2)
        logout_ele = self.get_element(self.re_login_locator)
        self.browser.execute_script("arguments[0].click();",logout_ele)
        time.sleep(3)
    def test_login_01(self):
        self.login('3401030307','000000')
        self.logout()
        #self.login('3401030307','000000')

if __name__=='__main__':
    #unittest.main()
    browser = webdriver.Chrome()
    loginpage = LoginPage(browser)
    loginpage.test_login_01()