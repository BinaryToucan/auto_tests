from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.ID, "book")
    
    price = WebDriverWait(browser, 5).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button.click()

    input_value = browser.find_element(By.ID, "input_value")
    answer = calc(input_value.text)

    select = browser.find_element(By.ID, "answer")
    select.send_keys(answer)

    button = browser.find_element(By.ID, "solve")
    button.click()

    browser.find_element(By.ID, "button")

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()