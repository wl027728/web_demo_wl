# -*- coding: utf-8 -*-
"""
    Create Time: 2019/7/9 20:53
    Author: 作者
"""
import datetime,json
import string,random
import cx_Oracle

import pymysql

from scripts.handel_config import config


class HandleMysql1:
    def __init__(self):
        self.conn =cx_Oracle.connect('ccic_uat_pub/ccic_uat_pub@10.2.3.195:1521/pnccicuat')
        self.cursor = self.conn.cursor()

    def get_sql_result(self, sql,is_more= False):
        self.cursor.execute(sql)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()
        # dict_data = []
        # key = [item[0] for item in self.cursor.description]
        # for value in self.cursor.fetchall():
        #     dict_data.append(dict(zip(key,value)))
        # a = dict_data[0].get('MESSAGE')
        # print(a)
        # print(type(a))


    def close(self):
        self.cursor.close()
        self.conn.close()

sql_re = [{'INSERT_BY': -11, 'UPDATE_BY': 26004850599, 'INSERT_TIME': datetime.datetime(2020, 4, 17, 16, 52, 50), 'UPDATE_TIME': datetime.datetime(2020, 4, 17, 16, 52, 51), 'ID': 'a0b1dcda-9913-4df3-af0b-c8749dddb7c5',
          'CONTENT': '{"DeparturePortCode":"PLGDA-GDANSK","ClaimPayableAt":"SZCZECIN  IN  CNY","DepartureContinentCode":"EU-Europe","DestinationContinentCode":"EU-Europe","TrackingNo":null,"SignDate":"7/11/19","InvoiceAmount":"100000","DepartureDatePrint":"1/7/20","BillNumber":null,"DestinationCountryCode":"POL-POLAND","Insurant":{"PartyCategory":"01-个人","IndiIdType":"113-户口簿","CustomerName":"桑桑1","IdNo":"123"},"DepartureDate":"10/7/20","InvoiceNumber":"234324","TransportType":"06-公路","PremiumCurrencyCode":"CNY-人民币（CNY）","DepartureCountryCode":"POL-POLAND","InvoiceCurrency":"CNY-人民币（CNY）","SiCurrencyCode":"CNY-人民币（CNY）","OriginalQuantity":"2","Holder":{"PartyCategory":"01-个人","IndiIdType":"113-户口簿","CustomerName":"桑桑1","IdNo":"123"},"DepartureAddress":"GDANSK","ConveyanceInfo":"船舶","DestinationPortCode":"PLGDS-SZCZECIN","Insured":[{"CargoName":"原煤，煤炭，洗精煤，块煤，洗、选煤，水煤浆，其他煤（蜂窝煤等煤制品）","SumInsured":"100000","CoverageCode":"C100956-海洋货运损失-一切险","CargoType":"A01-原煤，煤炭，洗精煤，块煤，洗、选煤，水煤浆，其他煤（蜂窝煤等煤制品）","MainClauseCode":"CF1100055-协会货物保险（A）","PremiumRate":"10"},{"CargoName":null,"SumInsured":null,"CoverageCode":null,"CargoType":null,"MainClauseCode":null,"PremiumRate":null},{"CargoName":null,"SumInsured":null,"CoverageCode":null,"CargoType":null,"MainClauseCode":null,"PremiumRate":null},{"CargoName":null,"SumInsured":null,"CoverageCode":null,"CargoType":null,"MainClauseCode":null,"PremiumRate":null},{"CargoName":null,"SumInsured":null,"CoverageCode":null,"CargoType":null,"MainClauseCode":null,"PremiumRate":null}],"DestinationAddress":"SZCZECIN","InspectionAgent":"A258-JG-Marine Sp z.o.o. (WECCG Survey Agent)","CreditNumber":null,"PlusRatio":"100","PriceCondition":null}',
           'TASK_ID': 3008972840230636, 'LINE_NUM': 2, 'ERROR': None,
           'MESSAGE': '{"ProposalNo":"TYIE20340100104999990043","UsingTime":"0S","ContentId":"a0b1dcda-9913-4df3-af0b-c8749dddb7c5"}', 'EX_CONTENT': None}]

task_num = 3008972840230636
if __name__ =='__main__':
    run_mysql = HandleMysql1()
    task_num = 3008972840231648
    sql = 'select MESSAGE from t_pub_upload_content where task_id = %s '%task_num
    result = run_mysql.get_sql_result(sql)
    result_dict = json.loads(result[0],encoding='utf-8')
    print(result_dict)
    print(result_dict.get('ProposalNo'))