from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
#建立一个浏览器对象
driver = webdriver.Firefox()
#启动页面
driver.get('https://www.baidu.com')
# driver.set_window_size(800,600)
# driver.find_element_by_id('kw').send_keys('万门大学')
# driver.find_element_by_id('su').click()
# driver.implicitly_wait(10)
#
setup = driver.find_element_by_id('s-usersetting-top')
#
ActionChains(driver).move_to_element(setup).perform()
# driver.find_element_by_link_text('高级搜索').click()
# sleep(1)
# driver.find_element_by_id('adv_keyword').send_keys('123123123')
# driver.implicitly_wait(10)
# driver.find_element_by_class_name('competition__detail-title--2Hl4V').click()
print(driver.current_window_handle)


driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/a[6]').click()

allwindows = driver.window_handles
driver.switch_to.window(allwindows[-1])
sleep(10)
# print(driver.current_window_handle)
# driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[2]/div[3]/div[2]/div[2]/div[1]/div[1]/div/ul/li[2]/a').click()
driver.find_element_by_link_text('英雄联盟').click()
sleep(2)
# print(driver.current_window_handle)
print(driver.window_handles)


# driver.find_element_by_id('kw').send_keys('abcd')
# driver.implicitly_wait(10)
# driver.find_element_by_id('su').click()
