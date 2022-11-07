import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
# def driver():
    # # service = ChromeService(executable_path=ChromeDriverManager().install())
    # # driver = webdriver.Chrome(service=service)
    # yield driver
    # driver.quit()

def driver():
    o = webdriver.ChromeOptions()
    o.headless = True
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),options=o
    )
    yield driver
    driver.quit()