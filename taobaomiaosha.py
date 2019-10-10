#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 2018/09/05
# 淘宝秒杀脚本，扫码登录版
import os
from selenium import webdriver
import datetime
import time
from os import path

from selenium.webdriver.common.action_chains import ActionChains

d = path.dirname(__file__)
abspath = path.abspath(d)

driver = webdriver.Firefox()
driver.maximize_window()


def login(username, password):
    # 打开淘宝登录页，并进行扫码登录
    driver.get("http://scbm.cltt.org/pscw/login.html")

    time.sleep(3)
    driver.add_cookie({'realName': '13228108248', 'SESSION': 'ZWY3MzA4OTctZTVkMi00ZThiLThlYmItNWNjMTY2MTlkM2Ri', '_uab_collina': '156962736270202571024051', 'td_cookie': '1941117348', 'aliyungf_tc': 'AQAAAH86OCwKQQ0A/RfPZZrW5/6RImQB'})
    # 存储着用户登录状态的
    driver.add_cookie({'realName': '13228108248', 'SESSION': 'ZWY3MzA4OTctZTVkMi00ZThiLThlYmItNWNjMTY2MTlkM2Ri', '_uab_collina': '156962736270202571024051', 'td_cookie': '1941117348', 'aliyungf_tc': 'AQAAAH86OCwKQQ0A/RfPZZrW5/6RImQB'})
    time.sleep(15)
    # driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(0.01)

    if driver.find_element_by_id("J_SelectAll1"):
        driver.find_element_by_id("J_SelectAll1").click()
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
    while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # 对比时间，时间到的话就点击结算
        if now > buytime:
            try:
                # 点击结算按钮
                if driver.find_element_by_id("J_Go"):
                    driver.find_element_by_id("J_Go").click()
                driver.find_element_by_link_text("提交订单").click()
            except:
                time.sleep(0.01)
                print(now)
                time.sleep(0.01)


if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    login('13228108248', 'MuXu2014')
    buy("2019-05-09 17:07:00.000000")