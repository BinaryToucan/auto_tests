from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    val = browser.find_element(By.ID, "treasure")
    value = val.get_attribute("valuex")
    answer = calc(value)
    inputBox = browser.find_element(By.ID, "answer")
    inputBox.send_keys(answer)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobox = browser.find_element(By.ID, "robotsRule")
    radiobox.click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла