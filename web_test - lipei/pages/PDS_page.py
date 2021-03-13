
# -*- coding: utf-8 -*-
"""
    Create Time: 2020/6/19 15:14
    Author: 作者
"""
import time
import unittest
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scripts.constants import LOG_IMG_DIR
from scripts.handle_logging import logger
from selenium.webdriver.support.select import Select
from pages.base_page import Element,BasePage
from pages.login_page import LoginPage
from locator.common_locator import CommonL
from pages.home_page import HomePage
from selenium.webdriver.common.action_chains import ActionChains
from scripts.handle_parameter import HandleParam
from pages.casequery_page import CaseQueryPage


class PropertydsPage(BasePage):
    PDShandle_button_locator = (By.XPATH,"//td[text()='财产定损']/following-sibling::td[10]/a[2][contains(@data-task,'${caseno}')]")#财产险处理按钮
    choseTK_locator = (By.NAME,"propertyDamageClause[0]")#选择条款
    unit_locator = (By.CSS_SELECTOR,"#damage-property table td:nth-child(4) input ")#单价
    num_locator = (By.CSS_SELECTOR, "#damage-property table td:nth-child(5) input ")  # 数量
    unit_name_locator = (By.CSS_SELECTOR, "#damage-property table td:nth-child(6) input:nth-child(1)")  # 单价
    Pcommit_locator = (By.ID,"submitPropertyDamageBtn")#提交

    def inputPdsinfo(self):
        self.waite_visible_element(HandleParam.replace_caseno(self.PDShandle_button_locator))
        time.sleep(2)
        self.get_element(HandleParam.replace_caseno(self.PDShandle_button_locator)).click()
        time.sleep(5)
        self.switch_window_by_title('财产定损')
        if self.get_element_num(CommonL.close_risk_locator)==1:
            self.get_element(CommonL.close_risk_locator).click()
        time.sleep(1)
        #Select(self.get_element(self.choseTK_locator)).select_by_index(1)
        self.get_element(self.unit_locator).send_keys('4')
        self.get_element(self.num_locator).send_keys('3')
        self.get_element(self.unit_name_locator).send_keys('个')
        time.sleep(2)
        self.get_element(self.unit_name_locator).send_keys(Keys.ENTER)
        time.sleep(1)
        self.get_element(self.Pcommit_locator).click()

    def test(self):
        LoginPage(browser).login('8000506294', '000000')
        HomePage(browser).enter_dbpage()
        self.inputPdsinfo()






if __name__=='__main__':
    #unittest.main()
    browser = webdriver.Chrome()
    PropertydsPage(browser).test()
