import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    # Creating chrome driver
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield chrome_driver
    # Closing chrome driver
    chrome_driver.quit()
