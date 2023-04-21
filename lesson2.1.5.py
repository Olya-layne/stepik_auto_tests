from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    value_x = browser.find_element(By.ID, "treasure")
    x = value_x.get_attribute("valuex")
    assert x is not None, "Unable to read attribute"
    
    y = calc(x)
    
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    
    check = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    check.click()
    
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()