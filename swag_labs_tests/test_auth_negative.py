import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestNegativeAuthScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [("", "secret_sauce", "Epic sadface: "
                                                                                                 "Username is "
                                                                                                 "required"),
                                                                            ("standard_user", "", "Epic sadface: "
                                                                                                  "Password is "
                                                                                                  "required"), (
                                                                            "standard_user", "non_valid_password",
                                                                            "Epic sadface: Username and password do not match any user in this service"),
                                                                            ("locked_out_user", "secret_sauce",
                                                                             "Epic sadface: Sorry, this user has been locked out.")])
    # iteration #1 checks that username is required
    # iteration #2 checks that password is required
    # iteration #3 checks that the password is validated
    # iteration #4 checks that locked out user can't log in
    def test_negative_auth_scenarios(self, driver, username, password, expected_error_message):
        driver.get("https://www.saucedemo.com/")

        input_login = driver.find_element(By.ID, "user-name")
        input_password = driver.find_element(By.ID, "password")
        input_login.send_keys(username)
        input_password.send_keys(password)
        input_password.send_keys(Keys.ENTER)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error"))
        )

        error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert error.text == expected_error_message
