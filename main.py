from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

# load the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# get the web page
driver.get('https://www.google.com/')

# get the button you need
button = driver.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]')
button.click()

# waiting 100 seconds
time.sleep(100)

driver.quit()