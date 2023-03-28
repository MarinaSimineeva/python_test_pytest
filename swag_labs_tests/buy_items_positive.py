import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import INVENTORY_URL, CHECKOUT_FIRST_STEP, CHECKOUT_SECOND_STEP, CHECKOUT_SUCCESS_URL


class TestBuyItems:

    @pytest.mark.order
    @pytest.mark.positive
    def test_ordering_items(self, driver, login, add_items):

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )

        driver.find_element(By.ID, "checkout").click()
        actual_url = driver.current_url
        assert actual_url == CHECKOUT_FIRST_STEP

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

        input_name = driver.find_element(By.ID, "first-name")
        input_surname = driver.find_element(By.ID, "last-name")
        input_postal = driver.find_element(By.ID, "postal-code")

        input_name.send_keys("Test")
        input_surname.send_keys("Test Name")
        input_postal.send_keys("00000")

        driver.find_element(By.ID, "continue").click()
        actual_url = driver.current_url
        assert actual_url == CHECKOUT_SECOND_STEP

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "finish"))
        )

        driver.find_element(By.ID, "finish").click()
        actual_url = driver.current_url
        assert actual_url == CHECKOUT_SUCCESS_URL

        assert driver.find_element(By.CLASS_NAME, "complete-header").text == "Thank you for your order!"
        assert driver.find_element(By.CLASS_NAME, "complete-text").text == "Your order has been dispatched, and will " \
                                                                           "arrive just as fast as the pony can get " \
                                                                           "there!"
        assert driver.find_element(By.CLASS_NAME, "title").text == "Checkout: Complete!"

        back_button = driver.find_element(By.ID, "back-to-products")
        assert back_button.text == "Back Home"
        back_button.click()
        actual_url = driver.current_url
        assert actual_url == INVENTORY_URL


