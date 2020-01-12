from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('https://testautomationpactice.blogspot.com')
driver.maximize_window()

#working with allert, but I haven't found the good app for this practice
driver.find_element_by_xpath("")
driver.switch_to_allert().accept()
driver.switch_to_alert().dismiss()