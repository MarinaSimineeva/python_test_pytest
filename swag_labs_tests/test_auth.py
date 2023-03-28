from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import INVENTORY_URL


class TestPositiveAuthScenario:

    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.parametrize("username, password",
                             [("standard_user", "secret_sauce"), ("performance_glitch_user", "secret_sauce"),
                              ("problem_user", "secret_sauce")])
    # iteration #1 checks regular authorization scenario
    # iteration #2 checks performance glitch case
    # iterarion #3 checks specific user authorization scenario
    def test_regular_login(self, driver, username, password):
        driver.get("https://www.saucedemo.com/")

        input_login = driver.find_element(By.ID, "user-name")
        input_password = driver.find_element(By.ID, "password")
        input_login.send_keys(username)
        input_password.send_keys(password)
        input_password.send_keys(Keys.ENTER)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        actual_url = driver.current_url
        assert actual_url == INVENTORY_URL, "The authorized user isn't redirected to " \
                                                                         "inventory list "
        assert driver.find_element(By.ID, "shopping_cart_container").is_displayed(), "Inventory list isn't " \
                                                                                     "displayed "
        assert driver.find_element(By.CLASS_NAME, "app_logo").text == "Swag Labs", "Wrong inventory list title"
        assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed(), "Sorting dropdown " \
                                                                                            "isn't displayed "
