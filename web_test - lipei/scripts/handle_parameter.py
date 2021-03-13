# -*- coding: utf-8 -*-
"""
    Create Time: 2019/7/14 15:58
    Author: 作者
"""

import re

from scripts.handel_config import HandleConfig
from selenium.webdriver.common.by import By

class HandleParam():

    case_no = r'\$\{caseno\}'
    stage = r'\$\{stage\}'
    JDname = r'\$\{JDname\}'
    @classmethod
    def replace_caseno(cls,data):
        #cls.case_num = getattr(cls,'casenum')
        cls.case_num = 'RZKF42020000000000001509'
        if re.search(cls.case_no,data[1]):
            data= re.sub(cls.case_no,cls.case_num,data[1])
            data = (By.XPATH,data)
        return (data)

    @classmethod
    def replace_stage(cls,data):
        cls.stage1 = getattr(cls,'stage1')
        if re.search(cls.stage,data[1]):
            data= re.sub(cls.stage,cls.stage1,data[1])
            data = (By.XPATH,data)
        return (data)

    @classmethod
    def replace_JDnameandCaseno(cls, data):
          data = cls.replace_caseno(data)
          cls.JDname1 = getattr(cls,'JDname1')
          if re.search(cls.JDname, data[1]):
              data = re.sub( cls.JDname,cls.JDname1, data[1])
              data = (By.XPATH, data)
          return (data)

if __name__ == '__main__':

    handelpare = HandleParam()
    data = (By.XPATH,'//td[text()="调解一级审核"]/following-sibling::td//a[text()="${caseno}"]')
    result = handelpare.replace_case(data)
    print(result)



