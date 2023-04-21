from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    value_x = browser.find_element(By.ID, "num1")
    x = int(value_x.text)
    value_y = browser.find_element(By.ID, "num2")
    y = int(value_y.text)
    
    target_value = str(x + y)
    print(target_value)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(target_value)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()