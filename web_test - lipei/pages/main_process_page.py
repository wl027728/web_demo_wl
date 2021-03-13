
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


class MainProcessPage(BasePage):
    tg_locator = (By.XPATH,"//label[text()='审批意见']/following-sibling::div/label[1]/input")
    th_locator = (By.XPATH,"//label[text()='审批意见']/following-sibling::div/label[2]/input")
    SHcommit_button_locator = (By.XPATH,"//button[text()='提交'] ")
    tsk_confirm_locator = (By.XPATH,"//button[@id='dialog_1_sure']")
    JA_state_locator = (By.XPATH,"//span[text()='结案']/../following-sibling::div[2]//span")#结案状态
    last_car_link_locator = (By.XPATH,"//div[@class='statusimg'][last()]//a")#最后一个车辆定损节点超链接
    last2_car_link_locator = (By.XPATH, "//div[@class='statusimg'][last()-1]//a")  # 倒数第二个车辆定损超链接
    LAZProcess_LAJD_locator = (By.XPATH, "//div[@class='subtask'][1]//img")  # 立案子流程里立案节点
    LSZProcee_SPJD_locator = (By.XPATH, "//div[@class='statusimg']/div[contains(string(),'实赔')]/../following-sibling::div[1]//img") # 理算子流程里的实赔节点
    reopenZC_title_locator = (By.XPATH, "///div[@title='重开仲裁']")  # 重开仲裁流程
    ZC_locator = (By.XPATH,"//div[@title='仲裁']")#仲裁流程
    Rlawsuit_locator = (By.XPATH, "//div[@title='再审诉讼']")  #再审诉讼流程
    CKZProcess_CKJD_locator = (By.XPATH, "//div[@class='statusimg']/div[contains(string(),'查勘')]/../following-sibling::div[1]//img")  # 查勘子流程里查勘节点标志
    LAZProcee_sign_locator = (By.XPATH, "//span[text()='立案']/../following-sibling::div[1]/i")  # 立案子流程图标
    CKZProcess_sign_locator = (By.XPATH, "//span[text()='查勘']/../following-sibling::div[1]/i")  # 查勘子流程图标
    reopen_SH_locator = (By.XPATH, "//span[text()='重开高级审核 ']")  # 重开高级审核
    reopen1_locator = (By.XPATH, "//div[text()='重开赔案1']")  # 重开赔案1
    cancel_sign_locator = (By.XPATH, "//div[@id='workflow-page']/div")  # 注销章
    LS_state_locator = (By.XPATH,"//span[text()='理算']/../following-sibling::div[2]//span")#理算状态
    DS_state_locator = (By.XPATH, "//span[text()='定损']/../following-sibling::div[2]//span")  # 定损状态
    carDS_state_locator = (By.XPATH, "//span[text()='车辆定损']/../following-sibling::div[2]//span")  # 车辆定损状态
    peopleDS_state_locator = (By.XPATH, "//span[text()='财产定损']/../following-sibling::div[2]//span")  # 财产定损状态
    propertyDS_state_locator = (By.XPATH, "//span[text()='人伤定损 ']/../following-sibling::div[2]//span")  # 人伤定损状态
    PJDname_locator = (By.XPATH,"//span[text()='${stage}']")#立案
    LA_locator = (By.XPATH,"//span[text()='立案']")#立案
    LA_state_locator = (By.XPATH, "//span[text()='立案']/../following-sibling::div[2]//span")  # 立案状态
    CK_state_locator = (By.XPATH,"//span[text()='查勘']/../following-sibling::div[2]//span")#查勘状态
    lastSH_handle_sign_locator = (By.XPATH, "//div[@class='subtask']/a/div[contains(string(),'未处理')]//img")  # 最后未处理审核标志
    lastSH_handle_name_locator = (By.XPATH, "//div[@class='subtask']/a/div[contains(string(),'未处理')]/../../preceding-sibling::div[1]")  # 最后未处理审核节点名称
    lastSH_handle_ZH_locator = (By.XPATH, "//div[@class='subtask']/a/div[contains(string(),'未处理')]/../following-sibling::div//span[2]")  # 最后未处理审核节点帐号
    SlastSH_handle_sign_locator = (By.XPATH, "//div[@class='subtask'][position()=last()-1]/a/div[contains(string(),'未处理')]//img")  # 倒数第二个未处理审核标志
    SlastSH_handle_name_locator = (By.XPATH, "//div[@class='subtask'][position()=last()-1]/a/div[contains(string(),'未处理')]/../../preceding-sibling::div[1]")  # 倒数第二个未处理审核节点名称
    SlastSH_handle_ZH_locator = (By.XPATH,"//div[@class='subtask'][position()=last()-1]/a/div[contains(string(),'未处理')]/../following-sibling::div//span[2]")  # 最倒数第二个未处理审核节点帐号
    SH_common_handle_locator = (By.XPATH,"//td[text()='${JDname}']/following-sibling::td[10]/a[2][contains(@data-task,'${caseno}')]")
    def checkprocessstate(self):
        time.sleep(5)
        self.switch_window_by_title('流程图')
        self.browser.refresh()
        self.waite_visible_element(self.LA_locator)
        time.sleep(2)
        PJD_namel = HandleParam.replace_stage(self.PJDname_locator)
        self.get_element(PJD_namel).click()
        time.sleep(2)
        num_ele = self.get_element_num(self.lastSH_handle_sign_locator)
        while num_ele >=1:
            JDstate = self.get_element(self.lastSH_handle_sign_locator).get_attribute('src')
            JDname = self.get_element(self.lastSH_handle_name_locator).get_attribute('innerText').split(':')[0]
            print(JDname)
            #self.JDZH = self.get_element(self.lastSH_handle_ZH_locator).text
            setattr(HandleParam, 'JDname1', JDname)
            if self.get_element_num(self.lastSH_handle_ZH_locator)==1:
                self.JDZH = self.get_element(self.lastSH_handle_ZH_locator).text
            else:
                self.JDZH == 'None'

            if self.JDZH == 'None':
                LoginPage(self.browser).login('0000000000','000000')
            else:
                self.browser = webdriver.Chrome()
                LoginPage(self.browser).login(self.JDZH,'000000')
                HomePage(self.browser).enter_dbpage()
                self.waite_visible_element(HandleParam.replace_JDnameandCaseno(self.SH_common_handle_locator))
                time.sleep(2)
                self.get_element(HandleParam.replace_JDnameandCaseno(self.SH_common_handle_locator)).click()
                time.sleep(5)
            self.switch_window_by_index(-1)
            time.sleep(10)
            if self.get_element_num(CommonL.close_risk_locator)==1:
                self.get_element(CommonL.close_risk_locator).click()
            time.sleep(2)
            tg_ele = self.get_element(self.tg_locator)
            self.browser.execute_script("arguments[0].click();",tg_ele)
            time.sleep(2)
            self.get_element(self.SHcommit_button_locator).click()
            self.waite_visible_element(CommonL.caseno_locator)
            time.sleep(2)
            self.get_element(CommonL.liuchen_sign_locator).click()
            time.sleep(2)
            time.sleep(5)
            self.switch_window_by_title('流程图')
            self.browser.refresh()
            self.waite_visible_element(self.LA_locator)
            time.sleep(2)
            PJD_namel = HandleParam.replace_stage(self.PJDname_locator)
            print(PJD_namel)
            self.get_element(PJD_namel).click()
            time.sleep(2)
            num_ele = self.get_element_num(self.lastSH_handle_sign_locator)

    def test(self):
        LoginPage(browser).login('8000506294', '000000')
        CaseQueryPage(browser).case_query()
        CaseQueryPage(browser).click_process_sign()
        self.checkprocessstate()






if __name__=='__main__':
    #unittest.main()
    browser = webdriver.Chrome()
    MainProcessPage(browser).test()
