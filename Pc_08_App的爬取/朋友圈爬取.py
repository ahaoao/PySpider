import os
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
from time import sleep
import time
import re

PLATFROM = 'Android'
DEVICE_NAME = 'GM1900'
APP_PACKAGE = 'com.tencent.mm'
APP_ACTIVITY = '.ui.LauncherUI'
DEVICE_SERVER = 'http://localhost:4723/wd/hub'
TIMEOUT = 40
MONGO_DB = 'moments'
MONGO_URL = 'localhost'
MONGO_COLLECTION = 'moments'
SCROLL_SLEEP_TIME = 1


class Moments():
    def __init__(self):
        """
        初始化
        """
        # 驱动配置
        self.desired_caps = {
            "platformName": PLATFROM,
            "deviceName": DEVICE_NAME,
            "appPackage": APP_PACKAGE,
            "appActivity": APP_ACTIVITY
        }
        self.driver = webdriver.Remote(DEVICE_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)
        self.client = MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]
        self.collection = self.db[MONGO_COLLECTION]
        # 处理器
        self.processor = Processor()

    def login(self):
        """
        模拟登陆
        """
        # 提示点击
        el1 = self.wait.until(
            EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        el1.click()

        el2 = self.wait.until(
            EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        el2.click()
        # 登陆按钮
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/edu')))
        login.click()
        # 手机输入
        phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/li')))
        phone.send_keys("18985242014")
        # 下一步
        el5 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/b0f')))
        el5.click()
        # 密码
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/li')))
        password.send_keys("MuXu2014")
        # 登陆
        submit = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/b0f')))
        submit.click()

        el8 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/b28')))
        el8.click()

        el9 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/b28')))
        el9.click()

    def enter(self):
        # 选项卡
        tab = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@resource-id, "com.tencent.mm:id/sh") and @bounds = "[637,2079][713,2134]"]')))
        tab.click()
        # 朋友圈
        moments = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@resource-id, "android:id/title") and @bounds = "[151,255][289,317]"]')))
        moments.click()

    def crawl(self):
        """
        爬取
        :return:
        """
        # 滑动点
        FLICK_START_X = 500
        FLICK_START_Y = 200
        FLICK_DISTANCE = 800
        while True:
            # 当前页面显示的所有状态
            items = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@resource-id="com.tencent.mm:id/eu8"]//android.widget.FrameLayout')))
            # 上滑
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y, 20000)
            # 遍历每条状态
            for item in items:
                try:
                    # 昵称
                    nickname = item.find_element_by_id('com.tencent.mm:id/b9i').get_attribute('text')
                    # 正文
                    content = item.find_element_by_id('com.tencent.mm:id/lu').get_attribute('text')
                    # 日期
                    date = item.find_element_by_id('com.tencent.mm:id/ep0').get_attribute('text')
                    # 处理日期
                    date = self.processor.date(date)
                    print(nickname, content, date)
                    data = {
                        'nickname': nickname,
                        'content': content,
                        'date': date,
                    }
                    # 插入MongoDB
                    # update使用$set操作符更新nickname和content的data数据
                    self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
                    sleep(SCROLL_SLEEP_TIME)
                except NoSuchElementException:
                    pass

    def main(self):
        # 登录
        self.login()
        # 进入朋友圈
        self.enter()
        # 爬取
        self.crawl()


class Processor():
    def date(self, datetime):
        """
        处理时间
        :param datetime: 原始时间
        :return: 处理后时间
        """
        if re.match('\d+分钟前', datetime):
            minute = re.match('(\d+)', datetime).group(1)
            datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - float(minute) * 60))
        if re.match('\d+小时前', datetime):
            hour = re.match('(\d+)', datetime).group(1)
            datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - float(hour) * 60 * 60))
        if re.match('昨天', datetime):
            datetime = time.strftime('%Y-%m-%d', time.localtime(time.time() - 24 * 60 * 60))
        if re.match('\d+天前', datetime):
            day = re.match('(\d+)', datetime).group(1)
            datetime = time.strftime('%Y-%m-%d', time.localtime(time.time()) - float(day) * 24 * 60 * 60)
        return datetime


if __name__ == '__main__':
    moments = Moments()
    moments.main()
