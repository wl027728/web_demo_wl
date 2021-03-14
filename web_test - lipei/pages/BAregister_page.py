# -*- coding: utf-8 -*-
"""
    Create Time: 2020/5/27 12:43
    Author: 作者
"""
import os,re
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
from selenium.webdriver.common.action_chains import ActionChains
from scripts.handle_parameter import HandleParam
from pages.home_page import HomePage
#from pages.main_process_page import MainProcessPage
from locator.common_locator import CommonL
class BaoAPage(BasePage):
    input_policyno_locator = (By.ID,'policyNo')
    search_locator = (By.ID,'mainSearch')
    BA_button_locator = (By.ID,'btn-regist')
    policyno_query_result_llocator = (By.XPATH,"//table[@id='policyTable']//tbody//td[3]")
    case_query_locator = (By.ID,"cnCaseQueryBtn")
    input_caseno_locator = (By.ID,"registNoOrPolicyNo")
    input_BApeople_locator = (By.NAME,'reportorName')
    input_BAphone_locator = (By.NAME,'reportorPhone')
    LXpeople_locator = (By.NAME,'linkerName')
    LXphone_locator = (By.NAME,'linkerPhone')
    BSmoney_locator = (By.NAME,'reportedLoss')
    changeArea_locator = (By.ID,'changeArea')
    input_damageLocation2_locator = (By.ID,'damageLocation')
    province_locator = (By.XPATH,"//div[@class='address_container']/div[2]/div[3]/span")
    city_locator = (By.XPATH,"//div[@class='address_container']/div[1]/div[3]/p/div[1]")
    area_locator = (By.XPATH,"//div[@class='address_container']/div[1]/div[3]/p/div[1]/p/span[1]")
    CXJG_locator = (By.ID,'damageRemark')
    submit_BA_locatro = (By.ID,'submitReport')
    detail_address_locator =(By.ID,'damageAddress')
    LAhandler_locator = (By.ID,'claimOrgan')
    CKhandler_locator = (By.ID, 'surveyOrgan')
    handler1_locator = (By.ID,'claimHandler')
    handler2_locator = (By.ID, 'surveyHandler')
    confirm_locator = (By.ID, 'dialog_1_sure')
    chose_BM_locator = (By.ID, '#bigAutocompleteContent table tr:nth-child(1) td div')
    submit_case_button_locator = (By.ID,'caseHandlerSubmit')
    submit_success_locator = (By.XPATH,"//div[text()='提交成功！']")
    caseno_locator = (By.XPATH,"//div[@class='dialog-success-taskNo']/div[2]")
    case_centor_locator = (By.XPATH, "//a[text()='案件中心']")  # 案件中心
    p_sign_locator = (By.XPATH, "//a[@data-title='报案登记']/div/button")  # 财产险报案登记标记
    arg_sign_locator = (By.XPATH, "//a[@data-title='报案登记']/span[1] ")  # 农险报案登记标记
    def counterreport(self,policyno):
        self.waite_visible_element(self.case_centor_locator)
        time.sleep(5)
        ActionChains(self.browser).move_to_element(self.get_element(self.case_centor_locator)).perform()
        time.sleep(2)
        if self.get_element_num(self.p_sign_locator)==1:
            self.get_element(self.p_sign_locator).click()
        if self.get_element_num(self.arg_sign_locator)==1:
            self.get_element(self.arg_sign_locator).click()
        time.sleep(10)
        self.switch_window_by_title('报案登记')
        self.waite_visible_element(self.input_policyno_locator)
        time.sleep(1)
        self.get_element(self.input_policyno_locator).send_keys(policyno)
        time.sleep(2)
        self.get_element(self.search_locator).click()
        time.sleep(1)
        self.waite_presence_element(self.policyno_query_result_llocator)
        time.sleep(1)
        self.get_element(self.BA_button_locator).click()
        time.sleep(2)
        self.switch_window_by_index(-1)
        self.waite_presence_element(self.input_BApeople_locator)
        time.sleep(1)
        self.scroll_element_intoview(self.get_element(self.input_BApeople_locator))
        self.get_element(self.input_BApeople_locator).send_keys('对方的')
        phone = self.fake.phone_number()
        self.get_element(self.input_BAphone_locator).send_keys(phone)
        self.get_element(self.LXpeople_locator).send_keys(phone)
        self.get_element(self.LXphone_locator).send_keys(phone)
        self.browser.execute_script('document.documentElement.scrollTop=30000')
        self.get_element(self.BSmoney_locator).send_keys('1000')
        Select(self.get_element(self.changeArea_locator)).select_by_visible_text('境内')
        self.get_element(self.input_damageLocation2_locator).click()
        time.sleep(1)
        self.get_element(self.province_locator).click()
        time.sleep(1)
        self.get_element(self.city_locator).click()
        time.sleep(1)
        self.get_element(self.area_locator).click()
        time.sleep(1)
        self.get_element(self.detail_address_locator).send_keys('1')
        self.get_element(self.CXJG_locator).send_keys('1')
        self.get_element(self.submit_BA_locatro).click()
        time.sleep(2)

    def casedispatch(self):
        self.waite_presence_element(self.handler1_locator)
        time.sleep(1)
        self.get_element(self.handler1_locator).send_keys('8000506294')
        self.get_element(self.handler1_locator).send_keys(Keys.ENTER)
        self.get_element(self.handler2_locator).send_keys('8000506294')
        self.get_element(self.handler2_locator).send_keys(Keys.ENTER)
        self.get_element(self.submit_case_button_locator).click()
        time.sleep(2)
        if self.get_element_num(self.confirm_locator)==1:
            self.get_element(self.confirm_locator).click()
        time.sleep(1)
        self.waite_presence_element(CommonL.caseno_locator)
        time.sleep(2)
        caseno = self.get_element(self.caseno_locator).text
        caseno = re.search(r'[a-zA-Z]+(\d)+',caseno).group()
        #self.browser.close()
        print(caseno)
        setattr(HandleParam,'casenum',caseno)
        setattr(HomePage,'caseno1',caseno)
        self.get_element(CommonL.task_sign_locator).click()
        time.sleep(2)

    def test_baoan(self):
        LoginPage(browser).login('3401030307','000000')
        self.counterreport('PZKF20310000000000090002')
        self.casedispatch()
        MainProcessPage(browser).checkprocessstate()





if __name__=='__main__':
    #unittest.main()
    browser = webdriver.Chrome()
    baoan = BaoAPage(browser)
    baoan.test_baoan()#RZKF42020000000000001394

