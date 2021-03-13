# -*- coding: utf-8 -*-
"""
    Create Time: 2020/6/29 15:23
    Author: 作者
"""
# -*- coding: utf-8 -*-
from selenium.webdriver import ActionChains

from pages.login_page import LoginPage

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
from  pages.main_process_page import MainProcessPage
from locator.common_locator import CommonL
from pages.danzhengshouji_page import UploadPage
from pages.casequery_page import CaseQueryPage
class YFPage(BasePage):
    YFadd_button_locator =(By.XPATH,"//span[contains(@class,'add-prepaidDetails')] ")#预付明细增加按钮
    YFmoney_locator = (By.XPATH,"//input[contains(@class,'feeAmtChange')] ")#预付金额输入框
    YFcost_button_locator = (By.XPATH,"//span[contains(@class,'add-directClaim')]")#预付费用明细增加按钮
    chose_cluase_locator = (By.CSS_SELECTOR,"div#directClaimInfo tbody tr td:nth-child(2) select")#条款
    cost_name_locator = (By.CSS_SELECTOR,"div#directClaimInfo tbody tr td:nth-child(4) select")#流费用名称
    cost_money_locator = (By.CSS_SELECTOR, "div#directClaimInfo tbody tr td:nth-child(5) input ")  # 费用金额
    totalAmount_locator = (By.ID, 'totalAmt')  # 预付汇总金额
    addPK1_button_locator = (By.XPATH, "//span[contains(@class,'add_acount_info')]")  # 赔款支付信息增加按钮第一行
    money_type_locator = (By.NAME, "compensateType0")  # 金额类型第一行
    LKpeo_type_locator = (By.NAME, "typePayeeName0")  # 领款人类型第一行
    pay_type_locator = (By.NAME, "payWay0")  # 支付方式第一行
    edit_locator = (By.XPATH,"//div[@id='indemnityPaidInfo']//tbody//tr[1]/td[5]")#编辑第一行
    PKmoney_locator = (By.NAME, "payMat0")  # 赔款金额第一行
    money_type2_locator = (By.NAME, "compensateType1")  # 金额类型第二行
    LKpeo_type2_locator = (By.NAME, "typePayeeName1")  # 领款人类型第二行
    pay_type2_locator = (By.NAME, "payWay1")  # 支付方式第二行
    PKmoney2_locator = (By.NAME, "payMat1")  # 赔款金额第二行
    PKJE_locator = (By.XPATH,"//label[text()='本次责任赔款']/../div//input")#赔款金额
    PKFY_locator = (By.XPATH, "//label[text()='本次费用']/../div//input")  # 赔款费用
    bank_name_locator = (By.ID,"bankName")#银行名称
    province_locator = (By.ID, "province")  # 输入省份
    city_locator = (By.ID, "city")  # 市
    KHH_locator = (By.ID, "bankoutlets")  # 输入开户行
    bank_num_locator = (By.ID, "bank_account")  # 输入卡号
    confirm_locator = (By.ID, "perBankInfoConfirm")  # 确定

    def createYFcalculationsheet(self):
        self.scroll_element_intoview(self.get_element(self.totalAmount_locator))
        time.sleep(1)
        self.get_element(self.totalAmount_locator).click()
        self.YFPK_money = self.get_element(self.PKJE_locator).text.replace('CNY','')

        self.YFPK_coast = self.get_element(self.PKFY_locator).text.replace('CNY','')

    def input_pkmoneyinfo(self,LKtype1,LKRtype,paytype1):
        self.get_element(self.addPK1_button_locator).click()
        time.sleep(1)
        Select(self.get_element(self.money_type_locator)).select_by_visible_text(LKtype1)
        Select(self.get_element(self.LKpeo_type_locator)).select_by_visible_text(LKRtype)
        Select(self.get_element(self.pay_type_locator)).select_by_visible_text(paytype1)
        if paytype1 == '集中支付-银行转账':
            self.input_BankAccountinfo()
        self.get_element(self.PKmoney_locator).send_keys(self.YFPK_money)

    def input_pkcostinfo(self,LKtype2,LKRtype,paytype2):
        self.get_element(self.addPK1_button_locator).click()
        time.sleep(1)
        Select(self.get_element(self.money_type2_locator)).select_by_visible_text(LKtype2)
        Select(self.get_element(self.LKpeo_type2_locator)).select_by_visible_text(LKRtype)
        Select(self.get_element(self.pay_type2_locator)).select_by_visible_text(paytype2)
        if paytype2 == '集中支付-银行转账':
            self.input_BankAccountinfo()
        self.get_element(self.PKmoney2_locator).send_keys(self.YFPK_coast)

    def input_BankAccountinfo(self,bankname,Kprovince,Kcity,bank,banknum):
        self.waite_visible_element(self.bank_name_locator)
        self.get_element(self.bank_name_locator).send_keys(bankname)
        time.sleep(1)
        self.get_element(CommonL.chose_first_locator).click()
        time.sleep(2)
        self.get_element(self.province_locator).send_keys(Kprovince)
        time.sleep(1)
        self.get_element(CommonL.chose_first_locator).click()
        time.sleep(2)
        self.get_element(self.city_locator).send_keys(Kcity)
        time.sleep(1)
        self.get_element(CommonL.chose_first_locator).click()
        time.sleep(2)
        self.get_element(self.KHH_locator).send_keys(bank)
        time.sleep(1)
        self.get_element(CommonL.chose_first_locator).click()
        time.sleep(2)
        self.get_element(self.bank_num_locator).send_keys(banknum)
        time.sleep(1)
        self.get_element(self.confirm_locator).click()
        time.sleep(1)


    def test_YFapply(self):
        LoginPage(self.browser).login('8000506294', '000000')
        CaseQueryPage(self.browser).case_query()
        CaseQueryPage(self.browser).apply_YF()



if __name__=='__main__':
    #unittest.main()
    browser = webdriver.Chrome()
    # chakan = ChaKanPage(browser)
    # chakan.test_chakan()#RZKF42020000000000001358 可用