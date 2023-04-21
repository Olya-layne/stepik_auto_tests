from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    #confirm = browser.switch_to.alert
    #confirm.accept()
    
    new_window = browser.window_handles[1]
    
    browser.switch_to.window(new_window)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    value_x = browser.find_element(By.ID, "input_value")
    x = int(value_x.text)
    assert x is not None, "Unable to read attribute"
    
    y = calc(x)
    
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()    
    
    
finally: 
    time.sleep(10)
    browser.quit()
    