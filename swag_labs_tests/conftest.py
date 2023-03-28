import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from data import AUTH_URL, regular_username, password
from helpers import list_items_chooser


@pytest.fixture()
def driver():
    # Creating chrome driver
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield chrome_driver
    # Closing chrome driver
    chrome_driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(AUTH_URL)
    input_login = driver.find_element(By.ID, "user-name")
    input_password = driver.find_element(By.ID, "password")
    input_login.send_keys(regular_username)
    input_password.send_keys(password)
    input_password.send_keys(Keys.ENTER)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )


@pytest.fixture()
def add_items(driver, login):
    inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    items_to_be_chosen = list_items_chooser(inventory_items)

    for i in items_to_be_chosen:
        i.find_element(By.TAG_NAME, 'button').click()

    return items_to_be_chosen
