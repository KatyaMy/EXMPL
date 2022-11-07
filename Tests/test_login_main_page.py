import time
import pytest
from selenium.webdriver.common.by import By


def test_open_web_page(driver):
    driver.get("https://www.saucedemo.com/")

    assert driver.title == "Swag Labs"
    time.sleep(2)


def test_login_page(driver):
    driver.get("https://www.saucedemo.com/")
    login_box = driver.find_element(By.ID, "user-name")
    login_box.send_keys("standard_user")
    password_box = driver.find_element(By.ID, "password")
    password_box.send_keys("secret_sauce")
    button = driver.find_element(By.ID, "login-button")
    button.click()
    time.sleep(3)
    if driver.title == "Swag Labs":
        print("CORRECT!")
    else:
        print("WRONG")
    driver.quit()
