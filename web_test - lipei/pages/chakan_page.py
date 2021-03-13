# -*- coding: utf-8 -*-
"""
    Create Time: 2020/6/29 15:23
    Author: 作者
"""
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
from pages.danzhengshouji_page import UploadPage
from pages.BAregister_page import BaoAPage
from pages.lian_page import LiAnPage
from  pages.home_page import HomePage
from scripts.handle_parameter import HandleParam
from pages.danzhengshouji_page import UploadPage
from pages.main_process_page import MainProcessPage
class ChaKanPage(BasePage):
    CKhandle_button_locator = (By.XPATH,"//td[text()='查勘']/following-sibling::td[10]/a[2][contains(@data-task,'${caseno}')]")#待办页面查勘处理按钮
    chakan_type_locator = (By.XPATH,"//select[contains(@name,'checkTaskVo')]")#查勘类型
    property_loss_locator = (By.XPATH,"//span[text()='财产']")#财产损失项
    RS_locator = (By.XPATH, "//span[text()='人伤']")  # 人伤损失项
    car_locator = (By.XPATH, "//span[text()='车辆']")  # 车辆损失项
    add_property_loss_locator = (By.XPATH, "//span[text()='增加财产损失标的']")  # 增加财产损失项
    add_RS_locator = (By.XPATH, "//span[text()='//span[text()='增加人伤损失标的']']")  # 人伤损失项
    add_car_locator = (By.XPATH, "//span[text()='增加车辆损失标的']")  # 车辆损失项
    risk_process_locator = (By.NAME,"damageRemark")#出险经过
    chakan_process_locator = (By.NAME, "checkRemark")  # 查勘过程
    ZRFX_locator = (By.NAME, "dutyAnalyze")  # 责任分析
    lossPG_locator = (By.NAME, "lossAnalyze")  # 损失评估
    Plossdetail_locator = (By.NAME, "lossDetail0")  # 财产损失标的明细
    Plossname_locator = (By.NAME, "woundedName1")  # 人伤损失姓名
    RSlossIDtype_locator = (By.NAME, "woundedIdentifyType1")  # 人伤损失证件类型
    RSlossID_locator = (By.NAME, "woundedIdentifyNo1")  # 人伤损失证件号码
    carlossCJH_locator = (By.NAME, "vinNo2")  # 车辆损失车架号
    carlossCPH_locator = (By.NAME, "licenseNo2")  # 人伤损失证件类型
    CKcommit_button_locator = (By.ID, "submitLossBtn")  # 查勘提交按钮
    BDlossname_locator = (By.NAME,'itemSel0')#损失标的名称
    JYJAS_button_locator = (By.XPATH,"//label[text()='是否简易赔案']/following-sibling::div/label[1]/input")#简易结案是按钮
    GSmoney_locator = (By.NAME,'sumLossFee')#估损金额

    def input_ck_basicinfo(self,losstype,chooseJYJA):
        if chooseJYJA == '是':
            setattr(UploadPage,'stage','简易结案')
        else:
            setattr(UploadPage,'stage','查勘')
        self.CKhandle_button_locator = HandleParam.replace_caseno(self.CKhandle_button_locator)
        self.waite_visible_element(self.CKhandle_button_locator)
        time.sleep(2)
        self.get_element(self.CKhandle_button_locator).click()
        time.sleep(5)
        self.switch_window_by_title('查勘登记')
        self.waite_click_element(self.CKcommit_button_locator)
        time.sleep(10)
        if self.get_element_num(CommonL.close_risk_locator)==1:
            self.get_element(CommonL.close_risk_locator).click()
        self.waite_visible_element(self.chakan_type_locator)
        time.sleep(1)
        Select(self.get_element(self.chakan_type_locator)).select_by_visible_text('现场查勘')
        if chooseJYJA == '是':
            self.get_element(self.JYJAS_button_locator).click()
            time.time(1)
            self.get_element(self.GSmoney_locator).send_keys('100')
        if losstype == '其他':
            self.get_element(self.RS_locator).click()
            self.get_element(self.car_locator).click()
            self.input_propertylossinfo()
            self.input_RSlossinfo()
            self.input_carlossinfo()
        if losstype == '财产':
            self.input_propertylossinfo()
        if losstype == '财人':
            self.get_element(self.RS_locator).click()
            self.input_propertylossinfo()
            self.input_RSlossinfo()



    def input_propertylossinfo(self):
        self.waite_presence_element(self.CKcommit_button_locator)
        time.sleep(1)
        self.scroll_element_intoview(self.get_element(self.add_property_loss_locator))
        time.sleep(1)
        self.get_element(self.add_property_loss_locator).click()
        self.waite_visible_element(self.Plossdetail_locator)
        time.sleep(1)
        self.get_element(self.Plossdetail_locator).send_keys('士大夫')
    def input_RSlossinfo(self,IDtype):
        self.waite_presence_element(self.CKcommit_button_locator)
        time.sleep(1)
        self.scroll_element_intoview(self.get_element(self.add_RS_locator))
        time.sleep(1)
        self.get_element(self.add_RS_locator).click()
        self.waite_visible_element(self.Plossname_locator)
        time.sleep(1)
        self.get_element(self.Plossname_locator).send_keys('dfdh')
        time.sleep(1)
        Select(self.get_element(self.RSlossIDtype_locator)).select_by_visible_text(IDtype)
        if IDtype=='身份证':
            self.get_element(self.RSlossID_locator).send_keys('32344332323232')
        elif IDtype=='户口簿':
            self.get_element(self.RSlossID_locator).send_keys('3234433')

    def input_carlossinfo(self,IDtype):
        self.waite_presence_element(self.CKcommit_button_locator)
        time.sleep(1)
        self.scroll_element_intoview(self.get_element(self.add_car_locator))
        time.sleep(1)
        self.get_element(self.add_car_locator).click()
        self.waite_visible_element(self.carlossCJH_locator)
        time.sleep(1)
        self.get_element(self.carlossCJH_locator).send_keys('LFV3A24G4E3030789')
        time.sleep(1)
        self.get_element(self.carlossCPH_locator).send_keys('363526352415243524')


    def commit_chakan(self):
        self.switch_window_by_title('查勘登记')
        time.sleep(1)
        self.get_element(self.risk_process_locator).send_keys('sfsdaf')
        self.get_element(self.chakan_process_locator).send_keys('sfsdaf')
        self.get_element(self.ZRFX_locator).send_keys('sfsdaf')
        self.get_element(self.lossPG_locator).send_keys('sfsdaf')
        time.sleep(1)
        self.get_element(self.CKcommit_button_locator).click()

    def test_chakan(self):
        # LoginPage(self.browser).login('3401030307', '000000')
        # BaoAPage(self.browser).counterreport('PZKF20310000000000090002')
        # BaoAPage(self.browser).casedispatch()
        # browser = webdriver.Chrome()
        # LoginPage(browser).login('8000506294', '000000')
        # HomePage(browser).enter_dbpage()
        # LiAnPage(browser).enter_LApage()
        # LiAnPage(browser).input_BDlossinfo()
        # LiAnPage(browser).input_LPcostinfo()
        # LiAnPage(browser).commit_lian()
        # MainProcessPage(browser).checkprocessstate()
        #self.browser = webdriver.Chrome()
        LoginPage(self.browser).login('8000506294', '000000')
        HomePage(self.browser).enter_dbpage()
        self.input_ck_basicinfo('财产','否')
        UploadPage(self.browser).upload_DZ(r'C:\list.xlsx')
        self.commit_chakan()


if __name__=='__main__':
    #unittest.main()
    browser = webdriver.Chrome()
    chakan = ChaKanPage(browser)
    chakan.test_chakan()#RZKF42020000000000001358 可用