import pytest
from selenium.webdriver.common.by import By
from helpers import inventory_titles_searcher, inventory_prices_searcher


class TestInventoryTabSorting:

    @pytest.mark.inventory
    @pytest.mark.positive
    def test_inventory_sorting(self, driver, login):

        inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item_label")
        title_list = inventory_titles_searcher(inventory_items)
        title_list_alphabetical = sorted(title_list)

        assert title_list_alphabetical == title_list, 'List of items is not alphabetically sorted by default'

        sorting_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        sorting_dropdown.click()
        sorting_dropdown.find_element(By.CSS_SELECTOR, "option[value='za']").click()

        inventory_items = driver.find_elements(By.CLASS_NAME, "inventory_item_label")
        title_list = inventory_titles_searcher(inventory_items)
        title_list_reverse = sorted(title_list, reverse=True)

        assert title_list_reverse == title_list, 'List of items is not reverse alphabetically sorted'

        sorting_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        sorting_dropdown.click()
        sorting_dropdown.find_element(By.CSS_SELECTOR, "option[value='lohi']").click()
        inventory_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices_list = inventory_prices_searcher(inventory_prices)

        prices_low_high = sorted(prices_list)
        assert prices_low_high == prices_list

        sorting_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        sorting_dropdown.click()
        sorting_dropdown.find_element(By.CSS_SELECTOR, "option[value='hilo']").click()

        inventory_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices_list = inventory_prices_searcher(inventory_prices)

        prices_high_low = sorted(prices_list, reverse=True)
        assert prices_high_low == prices_list