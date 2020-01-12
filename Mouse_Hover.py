from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('https://opensource-demo.orangehrmlive.com')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys('Admin')    #Enter Login
driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('admin123')    #Enter Password
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()                     #Click Login button

admin = driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')     #Find Admin button and save to variable
usermgnt = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')     #Find User management button and save to variable
users = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')       #Find Users button and save to variable

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermgnt).move_to_element(users).click().perform()       #Go from Admin to User management and to Users

time.sleep(3)
driver.quit()