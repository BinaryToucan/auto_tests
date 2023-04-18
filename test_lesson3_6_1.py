import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import math

email = ""
password = ""
timeout = 20
arr = [236895 + i for i in range(5)] + [236903 + i for i in range(3)]

ans = []

@pytest.mark.parametrize('number', arr) #8
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)

    login = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.navbar__auth_login'))
    )
    login.click()

    login = browser.find_element(By.XPATH, '//a[@data-tab-name="login"]')
    login.click()

    email_input = browser.find_element(By.ID, 'id_login_email')
    email_input.send_keys(email)

    password_input = browser.find_element(By.ID, 'id_login_password')
    password_input.send_keys(password)

    button = browser.find_element(By.CSS_SELECTOR, ".button_with-loader")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    try:
        _ = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".again-btn"))
        )
    except:

        textarea = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )        

        answer = math.log(int(time.time()))
        textarea = browser.find_element(By.CSS_SELECTOR, "textarea")
        textarea.send_keys(answer)

        button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        button.click()

    finally:
        answer = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )

        answer = answer.text
        assert answer == "Correct!", f"Not work! {answer}"
        ans.append(answer)
        print(ans)

