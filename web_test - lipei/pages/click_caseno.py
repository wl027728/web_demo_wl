# -*- coding: utf-8 -*-
"""
    Create Time: 2020/6/2 15:56
    Author: 作者
"""

# -*- coding: utf-8 -*-
"""
    Create Time: 2020/5/27 12:43
    Author: 作者
"""
import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scripts.constants import LOG_IMG_DIR
from scripts.handle_logging import logger

from pages.base_page import Element,BasePage
from pages.login_page import LoginPage
from selenium.webdriver.common.action_chains import ActionChains



class Click(BasePage):

    commit_DS_locator =(By.XPATH,"//input[@value='提交']")

    car_caseno_locator = (By.XPATH,"//td[text()='人伤跟踪']/following-sibling::td//a[text()='RZKF42020000000000000039']")


    def click_no(self):
        self.waite_presence_element(self.car_caseno_locator)
        time.sleep(1)
        self.get_element(self.car_caseno_locator).click()
        time.sleep(2)
        self.switch_window_by_title('人伤定损平台')
        time.sleep(2)
        flag = self.is_elemeny_exit(self.commit_DS_locator)
        print(flag)
        while not flag:
            #self.browser.close()
            ActionChains(browser).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
            self.switch_window_by_title('财意理赔')
            self.get_element(self.car_caseno_locator).click()
            time.sleep(2)
            self.switch_window_by_title('人伤定损平台')
            time.sleep(2)
            flag = self.is_elemeny_exit(self.commit_DS_locator)
        # if  not self.is_elemeny_exit(self.commit_DS_locator):
        #     self.browser.close()
        #     #self.switch_window_by_title('财意理赔')
        #     self.get_element(self.car_caseno_locator).click()
        #     if not self.is_elemeny_exit(self.commit_DS_locator):
        #         self.browser.close()
        #         # self.switch_window_by_title('财意理赔')
        #         self.get_element(self.car_caseno_locator).click()
        #         if not self.is_elemeny_exit(self.commit_DS_locator):
        #             self.browser.close()
        #             # self.switch_window_by_title('财意理赔')
        #             self.get_element(self.car_caseno_locator).click()


    def test_click(self):
        LoginPage(browser).login('3401030307', '000000')
        self.click_no()


if __name__=='__main__':
    browser = webdriver.Chrome()
    baoan = Click(browser)
    baoan.test_click()



