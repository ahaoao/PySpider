from selenium import webdriver
from selenium.webdriver import ActionChains


browser = webdriver.Chrome()
url = 'https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
# 起点
source = browser.find_elements_by_css_selector('#draggable')
# 终点
target = browser.find_elements_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()