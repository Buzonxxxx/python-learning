# https://selenium-python.readthedocs.io/index.html
# https://pypi.org/project/selenium/
# Cheatsheet: http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/
# WebDriver API: https://selenium-python.readthedocs.io/api.html

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

driver.get('https://www.saucedemo.com/')

# Check if the webpage title contains 'Swag Labs'
assert 'Swag Labs' in driver.title

driver.implicitly_wait(2)
logo = driver.find_element(By.CLASS_NAME, "login_logo")
login_button = driver.find_element(By.CLASS_NAME, "btn_action")

# Print the inner HTML of the logo (you can uncomment this for debugging)
# print(logo.get_attribute('innerHTML'))

# Assert that 'Swag Labs' is present in the page source
assert 'Swag Labs' in driver.page_source

# Find the username and password text fields by their IDs
username_textfield = driver.find_element(By.ID, 'user-name')
password_textfield = driver.find_element(By.ID, 'password')

# Clear the username and password text fields and input values
username_textfield.clear()
username_textfield.send_keys('standard_user')

password_textfield.clear()
password_textfield.send_keys('secret_sauce')

login_button.click()

time.sleep(2)
title = driver.find_element(By.CSS_SELECTOR, '.title')

# Assert that the title text contains 'Products'
assert 'Products' in title.text


