import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():

    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    yield driver
    driver.quit()