from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('https://www.tut.by/')
driver.maximize_window()

#Working with Radio Buttons (Check_Boxes is the same work)

status = driver.find_element_by_xpath('//*[@id="aid18665"]').is_selected()   #False by default
print(status)

driver.find_element_by_xpath('//*[@id="aid18665"]').click()  #select radio button

status = driver.find_element_by_xpath('//*[@id="aid18665"]').is_selected()   #True after clicking
print(status)

driver.close()