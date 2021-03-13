# -*- coding: utf-8 -*-
"""
    Create Time: 2019/7/1 22:59
    Author: 作者
"""
import logging

from scripts.handel_config import config


class HandleLogging:

    def __init__(self):
        self.case_logger = logging.getLogger(config.get_value('log','logger_name'))
        self.case_logger.setLevel(config.get_value('log','logger_level'))
        console_handle = logging.StreamHandler()
        file_handle = logging.FileHandler(config.get_value('log','log_name'), encoding='utf-8')

        # 4 定义日志输出渠道的日志等级
        console_handle.setLevel(config.get_value('log','console_level'))
        file_handle.setLevel(config.get_value('log','file_level'))

        # 5.定义日志输入格式
        simple_formatter = logging.Formatter(config.get_value('log','simple_formatter'))
        complex_formatter = logging.Formatter(config.get_value('log','complex_formatter'))

        console_handle.setFormatter(simple_formatter)
        file_handle.setFormatter((complex_formatter))

        # 6 对接 将日志收集器与输出渠道进行对接
        self.case_logger.addHandler(console_handle)
        self.case_logger.addHandler(file_handle)

    def get_logger(self):
        return self.case_logger

logger = HandleLogging().get_logger()


if __name__ == '__main__':
    logger.debug("这个是一个debug级别的日志信息")
    logger.info("这个是一个info级别的日志信息")
    logger.warning("这个是一个warning级别的日志信息")
    logger.error("这个是一个error级别的日志信息")
    logger.critical("这个是一个critical级别的日志信息")
