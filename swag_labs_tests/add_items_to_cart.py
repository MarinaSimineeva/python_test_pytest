import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import list_items_chooser


class TestAddItemsToCart:

    @pytest.mark.cart
    @pytest.mark.positive
    def test_adding_items_to_cart(self, driver, login):

        inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        items_to_be_chosen = list_items_chooser(inventory_items)
        amount = len(items_to_be_chosen)
        titles_list = []
        descr_list = []
        prices_list = []

        for i in items_to_be_chosen:
            name = i.find_element(By.CLASS_NAME, "inventory_item_name").text
            descr = i.find_element(By.CLASS_NAME, "inventory_item_desc").text
            price = i.find_element(By.CLASS_NAME, "inventory_item_price").text
            titles_list.append(name)
            descr_list.append(descr)
            prices_list.append(price)
            i.find_element(By.TAG_NAME, 'button').click()

        cart_beige = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert int(cart_beige.text) == amount

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )

        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(cart_items) == amount
        for i in cart_items:
            index = cart_items.index(i)
            title = i.find_element(By.CLASS_NAME, "inventory_item_name").text
            descr = i.find_element(By.CLASS_NAME, "inventory_item_desc").text
            price = i.find_element(By.CLASS_NAME, "inventory_item_price").text
            assert title == titles_list[index]
            assert descr == descr_list[index]
            assert price == prices_list[index]
