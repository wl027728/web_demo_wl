# -*- coding: utf-8 -*-
"""
    Create Time: 2020/8/13 16:57
    Author: 作者
"""
# -*- coding: utf-8 -*-
"""
    Create Time: 2020/8/13 16:19
    Author: 作者
"""
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


class PeoplePage(BasePage):
    Pclause_locator = (By.NAME,"propertyDamageClause[0]")#定损条款
    price_locator = (By.CSS_SELECTOR,"#damage-property table td:nth-child(4) input")#单价
    num_locator = (By.CSS_SELECTOR,"#damage-property table td:nth-child(5) input")#
    unit_locator = (By.CSS_SELECTOR, "#damage-property table td:nth-child(6) input:nth-child(1)")  # 单位
    commit_locator = (By.ID, "submitPropertyDamageBtn")  # 提交按钮
    recall_locator = (By.XPATH, "retractPropertyDamage")  # 撤回按钮
    recall_success_locator = (By.XPATH,"//font[text()='撤回成功']")#撤回成功
    change_locator = (By.ID, "applyReAssign")  # 申请改派按钮
    Tpay_locator = (By.ID, "applyIndemnity")  # 申请通赔
    cancel_locator = (By.ID, "closePropertyDamage")  # 注销按钮
    changereason_locator = (By.XPATH, "//textarea[contains(@data-link,'cancelOrReassignContent')]")  # 申请改派原因
    confirm_chage_locator = (By.ID, "submitReassignmentInfo")  # 改派确定按钮
    name_locator = (By.ID, "informantName")  # 被委托人
    org_locator = (By.ID, "comCodeText")  # 被委托机构
    confirm_cancel_locator = (By.ID, "propertyDamageCancel")  # 注销确定
    DD_locator = (By.ID, "shedulInfoSubmit")  # 调度提交按钮
    cancel_success_process_locator = (By.XPATH, "//font[text()='注销成功']/../following-sibling::div[1]//div[@class='dialog-success-taskNo']/div[2]//img")  # 注销成功界面任务流图标
    addCK_locator = (By.XPATH,"//a[text()='新增查勘']")#新增查勘

    def input_propertylossinfo(self,clause,unitP,amount,unit):
        self.waite_presence_element(self.Pclause_locator)
        Select(self.get_element(self.Pclause_locator)).select_by_visible_text(clause)
        self.get_element(self.price_locator).send_keys(unitP)
        self.get_element(self.num_locator).send_keys(amount)
        self.get_element(self.unit_locator).send_keys(unitP,Keys.ENTER)
        self.get_element(self.commit_locator).click()
        self.waite_visible_element(CommonL.caseno_locator)
        time.sleep(1)
        self.get_element(CommonL.task_sign_locator).click()
        time.sleep(2)
        self.browser.close()



if __name__=='__main__':
    #unittest.main()
    browser = webdriver.Chrome()
    chakan = ChaKanPage(browser)
    chakan.test_chakan()#RZKF32020000000000323341