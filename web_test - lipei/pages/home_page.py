import os
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
from locator.common_locator import CommonL
from pages.base_page import Element,BasePage
from pages.login_page import LoginPage
from scripts.handle_parameter import HandleParam
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class HomePage(BasePage):

    # adjustYJcaseno_locator = (By.XPATH,'//td[text()="调解一级审核"]/following-sibling::td//a[text()="${caseno}"]')
    # RStrackcheckcaseno_locator = (By.XPATH,"//td[text()='人伤跟踪审核']/following-sibling::td//a[text()='${caseno}']")
    # RStrackcaseno_locator = (By.XPATH,"//td[text()='人伤跟踪']/following-sibling::td//a[text()='${caseno}']")
    # take_task_locator = (By.XPATH,"//a[contains(@class,'receive-tasks-btn')]")#领取任务
    # porpertyDS_caseno_locator = (By.XPATH,"//td[text()='财产定损']/following-sibling::td//a[text()='${caseno}']")
    # lajp_zzYJ_caseno_locator = (By.XPATH,"//td[text()='立案拒赔高级审核中支一级']/following-sibling::td//a[text()='${caseno}']")
    # lajp_fgsSJ_caseno_locator = (By.XPATH, "//td[text()='立案拒赔高级审核分公司四级']/following-sibling::td//a[text()='${caseno}']")
    # lajp_zgsYJ_caseno_locator = (By.XPATH, "//td[text()='立案拒赔高级审核总公司一级']/following-sibling::td//a[text()='${caseno}']")
    # CK_caseno_locator = (By.XPATH,"//td[text()='查勘']/following-sibling::td//a[text()='${caseno}']")
    # LA_caseno_locator = (By.XPATH,"//td[text()='立案']/following-sibling::td//a[text()='${caseno}']")
    # PDS_caseno_locator = (By.XPATH, "//td[text()='财产定损']/following-sibling::td//a[text()='${caseno}']")
    #close_risk_locator = (By.CSS_SELECTOR,".btn.btn-xs.btn-float-box-close")#关闭风险提示狂
    task_centor_locator = (By.XPATH,"//a[text()='任务中心']")#任务中心
    p_db_locator = (By.XPATH, "//a[@data-title='我的待办']/div/button[text()='财']")#财产险我的待办标记
    arg_db_locator = (By.XPATH, "//a[@data-title='我的待办']/span[1]")#农险我的待办标记
    db_inputcaseno_locator = (By.XPATH, "//input[@id='registNo']")#待办页面输入报案号
    all_locator = (By.XPATH, "//span[text()='全部']")
    db_query_locator = (By.ID,"myTasksQueryBtn") #待办查询按钮
    input_caseno_locator = (By.ID,"registNoOrPolicyNo")#报案号输入框
    confirm_locator = (By.ID, 'dialog_1_sure')


    def enter_dbpage(self):
        self.switch_window_by_title('财意理赔')
        self.browser.refresh()
        self.waite_visible_element(self.task_centor_locator)
        time.sleep(2)
        ActionChains(self.browser).move_to_element(self.get_element(self.task_centor_locator)).perform()
        time.sleep(2)
        if self.get_element_num(self.p_db_locator)==1:
            self.get_element(self.p_db_locator).click()
        if self.get_element_num(self.arg_db_locator)==1:
            self.get_element(self.arg_db_locator).click()
        time.sleep(10)
        self.switch_window_by_title('我的待办')
        self.waite_click_element(self.db_query_locator)
        time.sleep(1)
        self.get_element(self.all_locator).click()
        self.waite_click_element(self.db_query_locator)
        time.sleep(5)
        #caseno = getattr(self,'caseno1')
        self.get_element(self.db_inputcaseno_locator).send_keys('RZKF42020000000000001509')
        time.sleep(2)
        self.scroll_element_intoview(self.get_element(self.db_query_locator))
        time.sleep(1)
        self.get_element(self.db_query_locator).click()


if __name__=='__main__':
    unittest.main()
    browser = webdriver.Chrome()
    homepage = HomePage(browser)