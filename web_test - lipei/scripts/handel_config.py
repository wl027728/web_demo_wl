# -*- coding: utf-8 -*-
"""
    Create Time: 2019/7/1 19:44
    Author: 作者
"""
from configparser import ConfigParser

from scripts.constants import CONFIGS_FILE_PATH


class HandleConfig:

    def __init__(self,filename=None):
        self.filename = filename
        self.config = ConfigParser()
        self.config.read(self.filename,encoding='utf-8')

    def get_value(self,section,option):
        return self.config.get(section,option)

    def get_int(self,section,option):
        return self.config.getint(section,option)

    def get_float(self,section,option):
        return self.config.getfloat(section,option)

    def get_boole(self,section,option):
        return self.config.getboolean(section,option)

    def get_eval_data(self,section,option):
        return eval(self.config.getint(section,option))

    @staticmethod
    def write_config(datas,filename):
        config = ConfigParser()
        for key in datas:
            config[key] = datas[key]

        with open(filename,'w') as file:
            config.write(file)

config = HandleConfig(CONFIGS_FILE_PATH)
if __name__ =='__main__':

    # datas = {
    #     "file path": {'cases_path': 'cases.xlsx', 'log_path': 'record_run_result.txt'},
    #     "msg": {'success_result': 'Pass', 'fail_result': 'Fail'}
    # }
    # write_filename ='write_config.conf'
    # config.write_config(datas,write_filename)
     print(config.get_int('excel','actual_col'))


