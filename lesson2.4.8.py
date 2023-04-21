from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
       
    button.click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    next_action = browser.find_element(By.ID, "input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", next_action)
    
    value_x = browser.find_element(By.ID, "input_value")
    x = int(value_x.text)
    assert x is not None, "Unable to read attribute"
    
    y = calc(x)
    
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    
    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    
finally: 
    time.sleep(10)
    browser.quit()
