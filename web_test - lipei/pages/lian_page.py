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
from pages.main_process_page import MainProcessPage


class LiAnPage(BasePage):
    LAhandle_button_locator = (By.XPATH, "//td[text()='立案']/following-sibling::td[10]/a[2][contains(@data-task,'${caseno}')]")  # 待办页面查勘处理按钮
    lossBD_locator = (By.NAME,'itemSelLoss0')#损失标的
    commit_LA_button_locator = (By.ID,'submitClaimBtn')#立案提交按钮
    clause_locator = (By.CSS_SELECTOR,'#lossItemArea table tbody td:nth-child(3) select')#条款
    loss_detail_locator = (By.CSS_SELECTOR, '#lossItemArea table tbody td:nth-child(2) input')  # 损失明细
    LA_money1_locator = (By.CSS_SELECTOR, '#lossItemArea table tbody td:nth-child(5) input')  # 标的立案金额
    LA_money2_locator = (By.CSS_SELECTOR, '#estimatedClaimCostAear table tbody td:nth-child(5) input')  # 费用立案金额
    chose_FY_locator = (By.CSS_SELECTOR, '#estimatedClaimCostAear table tbody td:nth-child(4) select')  # 选择费用类型
    add_lpfy_button_locator = (By.CSS_SELECTOR, '#estimatedClaimCostAear [name=addItem]')  # 理赔费用增加按钮
    add_bdss_button_locator = (By.CSS_SELECTOR, '#lossItemArea [name=addItem]')  # 标的损失增加按钮
    lpfy_locator = (By.CSS_SELECTOR, '#estimatedClaimCostAear #claim-fee-type')  # 理赔费用
    bdss_locator = (By.XPATH, "//div[contains(text(),'标的损失')]")  # 标的损失

    def enter_LApage(self):

        self.LAhandle_button_locator = HandleParam.replace_caseno(self.LAhandle_button_locator)
        self.waite_click_element(self.LAhandle_button_locator)
        time.sleep(1)
        self.scroll_element_intoview(self.get_element(self.LAhandle_button_locator))
        time.sleep(1)
        self.get_element(self.LAhandle_button_locator).click()
        time.sleep(5)
        self.switch_window_by_title('立案')
        setattr(HandleParam,'stage1','立案')
        self.waite_click_element(self.commit_LA_button_locator)
        time.sleep(10)
        if self.get_element_num(CommonL.close_risk_locator)==1:
            self.get_element(CommonL.close_risk_locator).click()
        self.waite_visible_element(self.commit_LA_button_locator)
        time.sleep(1)
    def input_BDlossinfo(self):
        self.waite_presence_element(self.commit_LA_button_locator)
        time.sleep(1)
        self.browser.execute_script('document.documentElement.scrollTop=30000')
        self.get_element(self.bdss_locator).click()
        time.sleep(1)
        self.get_element(self.add_bdss_button_locator).click()
        time.sleep(1)
        lossBD_text = Select(self.get_element(self.lossBD_locator)).first_selected_option.text
        if lossBD_text=='':
            Select(self.get_element(self.lossBD_locator)).select_by_index('1')
        self.get_element(self.loss_detail_locator).send_keys('范德萨')
        Select(self.get_element(self.clause_locator)).select_by_visible_text('监护人责任保险(2012版)')
        self.get_element(self.LA_money1_locator).send_keys('100')

    def input_LPcostinfo(self):
        self.waite_presence_element(self.commit_LA_button_locator)
        time.sleep(1)
        self.browser.execute_script('document.documentElement.scrollTop=30000')
        self.get_element(self.lpfy_locator).click()
        time.sleep(1)
        self.browser.execute_script('document.documentElement.scrollTop=30000')
        self.get_element(self.add_lpfy_button_locator).click()
        time.sleep(2)
        Select(self.get_element(self.chose_FY_locator)).select_by_index('1')
        self.get_element(self.LA_money2_locator).send_keys('100')

    def commit_lian(self):
        time.sleep(1)
        self.get_element(self.commit_LA_button_locator).click()
        self.waite_presence_element(CommonL.caseno_locator)
        time.sleep(1)
        self.get_element(CommonL.task_sign_locator).click()
        time.sleep(2)
        #MainProcessPage(browser).checkprocessstate()

    def test_lian(self):
        LoginPage(browser).login('8000506294', '000000')
        HomePage(browser).enter_dbpage()
        self.enter_LApage()
        self.input_BDlossinfo()
        self.input_LPcostinfo()
        self.commit_lian()
        MainProcessPage(browser).checkprocessstate()

if __name__=='__main__':
    #unittest.main()
    browser = webdriver.Chrome()
    lian = LiAnPage(browser)
    lian.test_lian()#RZKF42020000000000000120