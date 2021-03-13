# -*- coding: utf-8 -*-
"""
    Create Time: 2019/8/28 14:37
    Author: 作者
"""
import os
import unittest
from datetime import datetime, time
from faker import Faker
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scripts.constants import LOG_IMG_DIR
from scripts.handle_logging import logger


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.fake = Faker(locale='zh_CN')

    def waite_presence_element(self, locator):
        '''等待元素出现'''
        try:
            return WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(locator))
        except Exception as e:
            print('加载超时')
            logger.error('错误原因是{}'.format(e))
            self.save_screenshot()
            raise e

    def waite_click_element(self, locator):
        '''等待一个可点击的元素，返回一个WebElement对象'''
        try:
            return WebDriverWait(self.browser, 60).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            print('加载超时')
            raise e

    def waite_visible_element(self, locator):
        try:
            return WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print('加载超时')
            raise e

    def save_screenshot(self):
        '''自动保存截图'''
        # 文件路径，配置文件去保存
        last_img_name = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S') + 'screen.png'
        img_name = os.path.join(LOG_IMG_DIR, last_img_name)
        return self.browser.save_screenshot(img_name)

    def get_element_num(self, locator):
        element = self.browser.find_elements(*locator)
        if len(element) == 0:
            return len(element)
        elif len(element) == 1:
            return len(element)
        else:
            print("找到%s个元素" % len(element))
            return 2

    def scroll_element_intoview(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView();",element)
        self.browser.execute_script('window.scrollBy(0,-200);')

    def get_element(self, locator) -> WebElement:
        return self.browser.find_element(*locator)

    def switch_window_by_title(self, title):
        for handle in self.browser.window_handles:
            self.browser.switch_to_window(handle)
            if self.browser.title.__contains__(title):
                break

    def switch_window_by_index(self, index):
        # 当前打开的所有窗口
        windows = self.browser.window_handles
        # 转换到最新打开的窗口
        self.browser.switch_to.window(windows[index])

    def get_time(offset_day):
        now_day = datetime.datetime.now()
        offset = datetime.timedelta(days=offset_day)  # 计算偏移量
        date = (now_day + offset).strftime('%Y-%m-%d')
        return date

    def double_click(self,element):
        '''双击操作'''
        action_chains = ActionChains(self.browser)
        action_chains.double_click(element).perform()

    #def up_load_file(self,element,filepath):
        elemnt_value = self.get_element()


class Element(object):
    def __init__(self, locator):
        self.locator = locator

    def __get__(self, instance, owner):
        '''定位元素'''
        web_elem = instance.browser.find_element(*self.locator)
        # self.web_element = web_elem
        return web_elem

    def click(self):
        self.web_element.click()

    def send_keys(self, data):
        self.web_element.send_keys(data)


if __name__ == '__main__':
    unittest.main()
    # browser = webdriver.Chrome()
    # loginpage = BasePage(browser)
    # loginpage.waite_presence_element((By.CSS_SELECTOR,'div.layui-layer-content'))
