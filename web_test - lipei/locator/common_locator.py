# -*- coding: utf-8 -*-
"""
    Create Time: 2020/6/19 16:08
    Author: 作者
"""

from selenium.webdriver.common.by import By


class CommonL():
    chose_first_locator = (By.CSS_SELECTOR,"#bigAutocompleteContent table tr:nth-child(1) td div")
    caseno_locator = (By.XPATH,"//div[@class='dialog-success-taskNo']/div[2]")#提交成功报案号
    close_risk_locator = (By.CSS_SELECTOR, ".btn.btn-xs.btn-float-box-close")  # 关闭风险提示狂
    task_sign_locator = (By.XPATH,"//span[contains(@class,'pointer registNo_ic_tree')] ")#提交结果页面上的任务流标志
    chakan_type_locator = (By.XPATH, "//select[contains(@name,'checkTaskVo')]")  # 查勘类型
    DZSJ_type_locator = (By.XPATH, "//a[text()='单证收集'] ")  # 单证收集
    liuchen_sign_locator = (By.XPATH,"//span[contains(@class,'pointer registNo_ic_tree')] ")# 任务流图标
    YFSQ1_locator = (By.XPATH, "//div[text()='预付申请']")  # 预付申请
    DHK_locator = (By.ID, 'rsb-daoru')  # 右边导航框
    tg_locator = (By.XPATH, "//label[text()='审批意见']/following-sibling::div/label[1]/input")
    th_locator = (By.XPATH, "//label[text()='审批意见']/following-sibling::div/label[2]/input")
    SHcommit_button_locator = (By.XPATH, "//button[text()='提交'] ")
    tsk_confirm_locator = (By.XPATH, "//button[@id='dialog_1_sure']")
    JA_state_locator = (By.XPATH, "//span[text()='结案']/../following-sibling::div[2]//span")  # 结案状态
    last_car_link_locator = (By.XPATH, "//div[@class='statusimg'][last()]//a")  # 最后一个车辆定损节点超链接
    last2_car_link_locator = (By.XPATH, "//div[@class='statusimg'][last()-1]//a")  # 倒数第二个车辆定损超链接
    LAZProcess_LAJD_locator = (By.XPATH, "//div[@class='subtask'][1]//img")  # 立案子流程里立案节点
    LSZProcee_SPJD_locator = (
    By.XPATH, "//div[@class='statusimg']/div[contains(string(),'实赔')]/../following-sibling::div[1]//img")  # 理算子流程里的实赔节点
    reopenZC_title_locator = (By.XPATH, "///div[@title='重开仲裁']")  # 重开仲裁流程
    ZC_locator = (By.XPATH, "//div[@title='仲裁']")  # 仲裁流程
    Rlawsuit_locator = (By.XPATH, "//div[@title='再审诉讼']")  # 再审诉讼流程
    CKZProcess_CKJD_locator = (By.XPATH,"//div[@class='statusimg']/div[contains(string(),'查勘')]/../following-sibling::div[1]//img")  # 查勘子流程里查勘节点标志
    LAZProcee_sign_locator = (By.XPATH, "//span[text()='立案']/../following-sibling::div[1]/i")  # 立案子流程图标
    CKZProcess_sign_locator = (By.XPATH, "//span[text()='查勘']/../following-sibling::div[1]/i")  # 查勘子流程图标
    reopen_SH_locator = (By.XPATH, "//span[text()='重开高级审核 ']")  # 重开高级审核
    reopen1_locator = (By.XPATH, "//div[text()='重开赔案1']")  # 重开赔案1
    cancel_sign_locator = (By.XPATH, "//div[@id='workflow-page']/div")  # 注销章
    LS_state_locator = (By.XPATH, "//span[text()='理算']/../following-sibling::div[2]//span")  # 理算状态
    DS_state_locator = (By.XPATH, "//span[text()='定损']/../following-sibling::div[2]//span")  # 定损状态
    carDS_state_locator = (By.XPATH, "//span[text()='车辆定损']/../following-sibling::div[2]//span")  # 车辆定损状态
    peopleDS_state_locator = (By.XPATH, "//span[text()='财产定损']/../following-sibling::div[2]//span")  # 财产定损状态
    propertyDS_state_locator = (By.XPATH, "//span[text()='人伤定损 ']/../following-sibling::div[2]//span")  # 人伤定损状态
    PJDname_locator = (By.XPATH, "//span[text()='${stage}']")  # 立案
    LA_locator = (By.XPATH, "//span[text()='立案']")  # 立案
    LA_state_locator = (By.XPATH, "//span[text()='立案']/../following-sibling::div[2]//span")  # 立案状态
    CK_state_locator = (By.XPATH, "//span[text()='查勘']/../following-sibling::div[2]//span")  # 查勘状态
    lastSH_handle_sign_locator = (By.XPATH, "//div[@class='subtask']/a/div[contains(string(),'未处理')]//img")  # 最后未处理审核标志
    lastSH_handle_name_locator = (
    By.XPATH, "//div[@class='subtask']/a/div[contains(string(),'未处理')]/../../preceding-sibling::div[1]")  # 最后未处理审核节点名称
    lastSH_handle_ZH_locator = (By.XPATH,
                                "//div[@class='subtask']/a/div[contains(string(),'未处理')]/../following-sibling::div//span[2]")  # 最后未处理审核节点帐号
    SlastSH_handle_sign_locator = (
    By.XPATH, "//div[@class='subtask'][position()=last()-1]/a/div[contains(string(),'未处理')]//img")  # 倒数第二个未处理审核标志
    SlastSH_handle_name_locator = (By.XPATH,
                                   "//div[@class='subtask'][position()=last()-1]/a/div[contains(string(),'未处理')]/../../preceding-sibling::div[1]")  # 倒数第二个未处理审核节点名称
    SlastSH_handle_ZH_locator = (By.XPATH,
                                 "//div[@class='subtask'][position()=last()-1]/a/div[contains(string(),'未处理')]/../following-sibling::div//span[2]")  # 最倒数第二个未处理审核节点帐号
    SH_common_handle_locator = (
    By.XPATH, "//td[text()='${JDname}']/following-sibling::td[10]/a[2][contains(@data-task,'${caseno}')]")