from selenium import webdriver
from selenium.webdriver.support.ui import Select  #For working with DropDown
import time

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()

element = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-9"]')
dropdown = Select(element)

# 1 Way: select_by_visible_text
dropdown.select_by_visible_text('Morning')
time.sleep(3)

# 2nd Way: select_by_index
dropdown.select_by_index(2)
time.sleep(3)

# 3rd Way: by Value
dropdown.select_by_value("Radio-2")
time.sleep(3)

driver.quit()


