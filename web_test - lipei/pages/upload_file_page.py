# -*- coding: utf-8 -*-
"""
    Create Time: 2020/4/8 15:55
    Author: 作者
"""

import os
import time
from datetime import datetime
import win32gui
import win32con
from dateutil.tz import win

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scripts.constants import LOG_IMG_DIR
from scripts.handle_logging import logger

from pages.base_page import Element,BasePage
from pages.login_page import LoginPage

class UploadFile(BasePage):

    drag_file = (By.XPATH,"//div[@class='dz-default dz-message']")

    drag_file_element = Element(drag_file)

    def uploadlist(self,filepath,browser_type="chrome"):
        self.drag_file_element.click()
        time.sleep(5)
        if browser_type == "chrome":
            title = "打开"
        else:
            title = ""
        dialog = win32gui.FindWindow("#32770",title)
        # 找元素
        # 一级窗口"#32770","打开"
        dialog = win32gui.FindWindow("#32770", title)
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        # 编辑按钮
        edit = win32gui.FindWindowEx(comboBox, 0, 'Edit', None)  # 四级
        # 打开按钮
        button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)")  # 四级

        # 往编辑当中，输入文件路径 。
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮





