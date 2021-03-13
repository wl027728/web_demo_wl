# -*- coding: utf-8 -*-
"""
    Create Time: 2019/7/9 20:53
    Author: 作者
"""

import string,random
import cx_Oracle

import pymysql

from scripts.handel_config import config


class HandleMysql:
    def __init__(self):
        self.conn = pymysql.connect(host = config.get_value('mysql','host'),
                               user = config.get_value('mysql','user'),
                               password = config.get_value('mysql', 'password'),
                               db = config.get_value('mysql','db'),
                               port=config.get_int('mysql','port'),
                               charset=config.get_value('mysql','charset'),
                               cursorclass=pymysql.cursors.DictCursor)#执行sql语句的结果为字典类型

        self.cursor = self.conn.cursor()

    def get_sql_result(self, sql, args=None, is_more=False):
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()



if __name__ =='__main__':
    run_mysql = HandleMysql()