from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.CLASS_NAME, "first_block .form-control.first")
    name.send_keys("Ir")
    surname = browser.find_element(By.CLASS_NAME, "first_block .form-control.second")
    surname.send_keys("Si")
    email = browser.find_element(By.CLASS_NAME, "first_block .form-control.third")
    email.send_keys("a@a.ru")
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()