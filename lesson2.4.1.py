from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")

    browser.find_element(By.ID, "button")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()