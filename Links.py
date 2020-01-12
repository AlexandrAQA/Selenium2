from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('http://newtours.demoaut.com')
driver.maximize_window()
links = driver.find_elements(By.TAG_NAME, "a")

print('Number of links in the page: ',len(links))    #Print how many links present in the page

for link in links:
    print(link.text)              #print all the link

#CLICKING ON THE LINK
driver.find_element(By.LINK_TEXT, "REGISTER").click()

#CLICKING ON THE LINK, when you know only part of link
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

time.sleep(3)
driver.close()