from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()

# 1. Scrolling down page by pixel
#driver.execute_script('window.scrollBy(0,1000)'," ")        # (0,1000) - Scrolling from Zero to 1.000 pixels and " " = 2 parameter is empty

# 2. Scroll down page till the element
#element = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[2]/tbody/tr[93]/td[2]') #Find the desired element (Ukraine), scroll to it
#driver.execute_script("arguments[0].scrollIntoView();",element)

# 3. Scroll down page till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)
driver.quit()