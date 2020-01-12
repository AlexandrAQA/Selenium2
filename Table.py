from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('file:///C:/Users/Alexandr/Downloads/html-td-background-css/html-td-background-css/html-td-background-css.html')
#driver.maximize_window()

rows = len(driver.find_elements_by_xpath("/html/body/div/div[2]/table/tbody/tr"))       #count number of rows
columns = len(driver.find_elements_by_xpath('/html/body/div/div[2]/table/tbody/tr[1]/th'))        #count number of columns
print('Number of rows: ',rows, '\nNumber of columns: ',columns)

driver.quit()