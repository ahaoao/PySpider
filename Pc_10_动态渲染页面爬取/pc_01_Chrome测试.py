from selenium import webdriver
import time


# 声明浏览器对象 browser 也支持Android手机端浏览器
browser = webdriver.Chrome()  # 谷歌
# browser = webdriver.Firefox() 火狐
# browser = webdriver.Edge()  windows
# browser = webdriver.Phantomjs() 无界面浏览器
# browser = webdriver.Safari()

# 访问页面
browser.get('https://www.taobao.com')
# print(browser.page_source)
# browser.close()

# 查找单个节点

input_first = browser.find_element_by_id('q')
# css选择器
input_second = browser.find_element_by_css_selector('#q')
# xpath选择器
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first, input_second, input_third)
browser.close()

# 通用方法 find_element()   它需要传入两个参数：查找方式By和值
# find_element_by_id(id) == find_element(By.ID, id)

# 多个节点
# find_elements()
input = browser.find_element_by_id('q')
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('ipad')
button = browser.find_element_by_class_name('btn-search')
button.click()

