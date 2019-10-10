from selenium import webdriver
import time


# 节点交互 输入文字用 send_keys()， 清空文字 clear()， 点击按钮click()
browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(2)
input.clear()
input.send_keys('ipad')
button = browser.find_element_by_class_name('btn-search')
button.click()

