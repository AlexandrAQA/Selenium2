from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('http://demo.automationtesting.in/Windows.html')
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
print(driver.current_window_handle)     #parent Window

handles = driver.window_handles     #Returns all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    time.sleep(2)
    if driver.title == 'Frames & windows':
        driver.close()

time.sleep(3)
driver.quit()