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
APP_PACKAGE = 'com.immomo.momo'
APP_ACTIVITY = '.android.activity.WelcomeActivity'
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

    def login(self):
        """
        模拟登陆
        """
        # 提示点击
        el1 = self.wait.until(
            EC.presence_of_element_located((By.ID, 'com.immomo.momo:id/iv_confirm')))
        el1.click()

        el2 = self.wait.until(
            EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        el2.click()

        el3 = self.wait.until(
            EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        el3.click()

        el4 = self.wait.until(
            EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button')))
        el4.click()

        # 登陆按钮
        login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.immomo.momo:id/tv_account_login')))
        login.click()

        # 手机输入
        phone = self.wait.until(EC.presence_of_element_located((By.ID, 'com.immomo.momo:id/login_et_momoid')))
        phone.send_keys("13228108248")
        # 密码
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'com.immomo.momo:id/login_et_pwd')))
        password.send_keys("MuXu2014")
        # 登陆
        submit = self.wait.until(EC.presence_of_element_located((By.ID, 'com.immomo.momo:id/btn_ok')))
        submit.click()

    def enter(self):

        # 附近的人
        e20 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@resource-id, "com.immomo.momo:id/tab_title") and @bounds = "[268,103][556,201]"]')))
        e20.click()
        # 筛选
        tab1 = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@resource-id, "com.immomo.momo:id/nearby_filter") and @bounds = "[949,126][1015,192]"]')))
        tab1.click()

        tab2 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.immomo.momo:id/nearby_filter')))
        tab2.click()

        tab3 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.immomo.momo:id/btn_ok')))
        tab3.click()

    def crawl(self):
        """
        爬取
        :return:
        """
        # 滑动点
        FLICK_START_X = 550
        FLICK_START_Y = 400
        FLICK_DISTANCE = 1600
        while True:
            # 当前页面显示的所有状态
            items = self.wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@resource-id="com.immomo.momo:id/user_layout_root"]//android.widget.RelativeLayout')))
            # 上滑
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y, 10000)
            # 遍历每条状态
            for item in items:
                try:
                    # 正文
                    content = item.find_element_by_id('com.immomo.momo:id/feed_textview').get_attribute('text')
                    # 图片
                    image = item.find_element_by_id('com.immomo.momo:id/feed_image_gridlayout').get_attribute('img')
                    img_path = 'img' + content
                    with open('content[1:3].jpg', 'wb') as f:
                        f.write(image)

                    # 日期
                    date = item.find_element_by_id('com.tencent.mm:id/ep0').get_attribute('text')

                    print(content, date)
                    data = {
                        'content': content,
                        'date': date,
                    }
                    # 插入MongoDB
                    # update使用$set操作符更新nickname和content的data数据
                    self.collection.update({'content': content}, {'$set': data}, True)
                    sleep(SCROLL_SLEEP_TIME)
                except NoSuchElementException:
                    pass

    def main(self):
        # 登录
        self.login()
        # 页面筛选
        self.enter()
        # 爬取
        self.crawl()


if __name__ == '__main__':
    moments = Moments()
    moments.main()
