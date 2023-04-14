from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    select = browser.find_element(By.NAME, "firstname")
    select.send_keys("AA")

    select = browser.find_element(By.NAME, "lastname")
    select.send_keys("AA")

    select = browser.find_element(By.NAME, "email")
    select.send_keys("AA")

    fileCheck = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    fileCheck.send_keys(file_path)


    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла