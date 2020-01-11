from selenium import webdriver
from selenium.webdriver.common.by import By

def Selenium_input_boxes():
    ''' 1.How to find how many inputBoxes present in web page
    2.How to provide value into text box
    3. How to get the status)'''

driver=webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')
driver.maximize_window()

# 1 How to find how many input boxes in the page
inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(inputboxes))

# 2 How to provide value into text box
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('Alex')
driver.find_element(By.ID,'RESULT_TextField-2').send_keys('Panaev')
driver.find_element_by_id('RESULT_TextField-3').send_keys('+375291234567')
driver.find_element_by_id('RESULT_TextField-4').send_keys('Belarus')
driver.find_element_by_id('RESULT_TextField-5').send_keys('Minsk')
driver.find_element_by_id('RESULT_TextField-6').send_keys('panaev.as@gmail.com')

#3 How to get the status
status1 = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print('Displayed or Not:',status1)  #True/False

status2 = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print('Enable or Not:', status2)

print('the program completed successfully')
driver.close()

