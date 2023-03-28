import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDeleteItemsFromCartScenarios:

    @pytest.mark.cart
    @pytest.mark.positive
    @pytest.mark.inventory
    def test_delete_items_on_inventory_screen(self, driver,login, add_items):
        cart_beige = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert int(cart_beige.text) == len(add_items)

        for i in add_items:
            i.find_element(By.TAG_NAME, 'button').click()

        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CLASS_NAME, "cart_item")

    @pytest.mark.cart
    @pytest.mark.positive
    def test_delete_items_from_cart_screen(self, driver, login, add_items):
        cart_beige = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert int(cart_beige.text) == len(add_items)

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")

        for i in cart_items:
            i.find_element(By.TAG_NAME, "button").click()

        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CLASS_NAME, "cart_item")

        driver.back()
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

