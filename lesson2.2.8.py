from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Ir")
    surname = browser.find_element(By.NAME, "lastname")
    surname.send_keys("Si")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("a@a.ru")
    
    upload = browser.find_element(By.ID, "file")
    
    
    current_dir = os.path.abspath(os.path.dirname(__file__))     
    file_path = os.path.join(current_dir, 'file.txt')           
    upload.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()
    
