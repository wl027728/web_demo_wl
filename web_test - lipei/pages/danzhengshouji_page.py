# -*- coding: utf-8 -*-
"""
    Create Time: 2020/7/1 17:15
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


class UploadPage(BasePage):
    applyYF_list_locator = (By.XPATH,"//div[text()='预付申请']")#清单里的预付申请
    CKJL_locator = (By.XPATH,"//div[text()='查勘清点记录']")#查勘清点记录
    DZsave_locator = (By.ID, "caseDocSubmitBtn")  # 单证收集保存按钮
    DZtype_locator = (By.ID, "level1")  # 单证类型框
    confirm_upload_DZ_locator = (By.XPATH, "//button[@id='dialog_1_sure']")  # 确定上传单证
    confirm_upload_file_locator = (By.XPATH, "//button[@class='confirm']")  # 确定上传文件
    finish_button_locator = (By.XPATH, "//div[@id='fileupload']/../following-sibling::div/div[8]")  # 完成按钮
    GL_locator = (By.XPATH,"//input[@id='autoUpload']/../../div[4]")#归类
    GLupload_locator = (By.ID, "autoUpload")  # 归类上传
    chose_file_locator = (By.XPATH, "//input[@ng-checked='fileIdxVo.checked']")  # 选择文件
    file_locator = (By.ID, "file-fr")  # 文件
    CKphoto_locator = (By.XPATH, "//td[text()='查勘照片']/following-sibling::td//i")  # 查勘照片
    YFSQ_locator = (By.XPATH, "//td[text()='预付申请']/following-sibling::td//i")  # 预付申请
    CKphoto1_locator = (By.XPATH, "//div[text()='查勘照片']")  # 查勘照片
    YFSQ1_locator = (By.XPATH, "//div[text()='预付申请']")  # 预付申请
    SmallM_locator = (By.XPATH,"//td[text()='小额案件理赔单']/following-sibling::td//i")#小额案件理赔单
    save_locator = (By.XPATH, "//div[text()='保存']")  # 保存按钮
    videoTB_locator = (By.XPATH, "//span[text()='影像数据同步']")  # 影像数据同步
    uploadDZ_locator = (By.XPATH, "//span[text()='单证上传']")  # 单证上传
    SPlist_locator = (By.XPATH, "//span[text()='索赔清单']")  # 索赔清单
    DHK_locator = (By.ID,'rsb-daoru')#右边导航框
    DZSJ_type_locator = (By.XPATH, "//a[text()='单证收集'] ")  # 单证收集


    def upload_DZ(self,filepath):
        self.waite_presence_element(self.DZSJ_type_locator)
        element = self.get_element(self.DZSJ_type_locator)
        ActionChains(self.browser).move_to_element(self.get_element(self.DHK_locator)).perform()
        time.sleep(1)
        self.get_element(self.DZSJ_type_locator).click()
        time.sleep(5)
        self.switch_window_by_title('资料收集')
        self.waite_visible_element(self.SPlist_locator)
        self.get_element(self.SPlist_locator).click()
        time.sleep(2)
        self.stage = getattr(self,'stage')
        if self.stage =='查勘':
            self.get_element(self.CKphoto_locator).click()
        elif self.stage =='预付申请':
            self.get_element(self.YFSQ_locator).click()
        elif self.stage == '简易结案':
            self.get_element((self.SmallM_locator)).click()
        time.sleep(1)
        self.get_element(self.save_locator).click()
        time.sleep(1)
        self.get_element(self.uploadDZ_locator).click()
        time.sleep(3)
        self.switch_window_by_title('H5影像系统管理')
        self.waite_presence_element(self.finish_button_locator)
        self.get_element(self.file_locator).send_keys(filepath)
        self.waite_presence_element(self.chose_file_locator)
        time.sleep(1)
        self.get_element(self.chose_file_locator).click()
        time.sleep(1)
        if self.stage =='查勘':
            Select(self.get_element(self.DZtype_locator)).select_by_visible_text('查勘类单证')
        elif self.stage =='预付申请':
            Select(self.get_element(self.DZtype_locator)).select_by_visible_text('索赔类单证')
        elif self.stage == '简易结案':
            Select(self.get_element(self.DZtype_locator)).select_by_visible_text('财物损失单证')
        self.get_element(self.GLupload_locator).click()
        self.get_element(self.GL_locator).click()
        self.get_element(self.finish_button_locator).click()
        self.get_element(self.confirm_upload_file_locator).click()
        self.switch_window_by_title('资料收集')
        time.sleep(5)
        self.get_element(self.videoTB_locator).click()
        time.sleep(1)
        self.get_element(self.confirm_upload_DZ_locator)
        time.sleep(1)


if __name__=='__main__':
    #unittest.main()
    browser = webdriver.Chrome()
