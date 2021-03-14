# -*- coding: utf-8 -*-
"""
    Create Time: 2020/6/29 15:23
    Author: 作者
"""
# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains

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
from scripts.handle_parameter import HandleParam
#from  pages.main_process_page import MainProcessPage
from locator.common_locator import CommonL
from pages.danzhengshouji_page import UploadPage
class CaseQueryPage(BasePage):
    input_caseno_locator = (By.ID,'registNoOrPolicyNo')#报案号输入框
    ARGsystem_query_button_locator =(By.XPATH,"//button[@id='cnCaseQueryBtn'] ")#农险页面查询按钮
    Psystem_query_button_locator = (By.XPATH,"//div[@id='search-box']/div/div/span/button[text()='案件查询' and contains(@style,'none')]")#财产险页面查询按钮
    pquery_button_locator = (By.XPATH,"//div[@id='search-box']/div/div/span/button[1]")#查询按钮_财产
    argquery_button_locator = (By.XPATH,"//div[@id='search-box']/div/div/span/button[2] ")#查询按钮_农
    process_sign_locator = (By.CSS_SELECTOR,"div#caseinfoshow_wrapper table tbody td:nth-child(11) a")#流程图标

    def case_query(self):
        self.waite_visible_element(self.input_caseno_locator)
        time.sleep(5)
        self.get_element(self.input_caseno_locator).send_keys('RZKF42020000000000001509')
        if self.get_element_num(self.ARGsystem_query_button_locator)== 1:
            self.get_element(self.ARGsystem_query_button_locator).click()
        if self.get_element_num(self.ARGsystem_query_button_locator)==0 and self.get_element_num(self.Psystem_query_button_locator)==0:
            self.get_element(self.pquery_button_locator).click()
        if self.get_element_num(self.Psystem_query_button_locator)==1:
            self.get_element(self.argquery_button_locator).click()
        time.sleep(5)
        self.switch_window_by_title('案件查询')
        self.waite_visible_element(self.process_sign_locator)
        time.sleep(2)
        setattr(HandleParam, 'stage1', '立案')

    def apply_YF(self):
        self.get_element(self.process_sign_locator).click()
        time.sleep(3)
        self.switch_window_by_title('流程图')
        self.browser.refresh()
        self.waite_visible_element(CommonL.LA_state_locator)
        time.sleep(2)
        self.get_element(CommonL.CK_state_locator).click()
        time.sleep(2)
        self.switch_window_by_title('查勘登记')
        time.sleep(5)
        if self.get_element_num(CommonL.close_risk_locator)==1:
            self.get_element(CommonL.close_risk_locator).click()
        self.waite_visible_element(CommonL.YFSQ1_locator)
        ActionChains(self.browser).move_to_element(self.get_element(CommonL.DHK_locator)).perform()
        time.sleep(1)
        self.get_element(CommonL.YFSQ1_locator).click()
        time.sleep(2)
        setattr(UploadPage, 'stage', '预付申请')

    def click_process_sign(self):
        self.get_element(self.process_sign_locator).click()
        time.sleep(5)




if __name__=='__main__':
    #unittest.main()
    browser = webdriver.Chrome()
    # chakan = ChaKanPage(browser)
    # chakan.test_chakan()#RZKF42020000000000001358 可用