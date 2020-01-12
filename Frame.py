from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\ChromeDriver\chromedriver.exe')
driver.get('https://seleniumhq.github.io/selenium/docs/api/java/index.html')
driver.maximize_window()

driver.switch_to.frame('packageListFrame')       # First Frame
driver.find_element_by_link_text('org.openqa.selenium').click()
#time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame('packageFrame')      # Second Frame
driver.find_element_by_link_text('WebDriver').click()
#time.sleep(3)

driver.switch_to.default_content()


driver.switch_to.frame('classFrame')        # Third Frame
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]/a').click()

time.sleep(3)
driver.quit()
