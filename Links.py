from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('http://newtours.demoaut.com')
links = driver.find_elements(By.TAG_NAME, "a")

print('Number of links in the page: ',len(links))    #Print how many links present in the page
