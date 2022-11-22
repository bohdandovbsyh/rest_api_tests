from selenium.webdriver.common.by import By

from framework_from_scratch_parsing.page_objects.dashboard_page import DashboardPage
from framework_from_scratch_parsing.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __email_input = (By.XPATH, '//input[@id="Email"]')
    __password_input = (By.CSS_SELECTOR, '#Password')
    __login_button = (By.XPATH, '//*[@type="submit"]')

    def set_email(self, email_value):
        self._send_keys(self.__email_input, email_value)
        return self

    def set_password(self, password_value):
        self._send_keys(self.__password_input, password_value)
        return self

    def click_login_button(self):
        self._click(self.__login_button)

    def login(self, email_value, password_value):
        self.set_email(email_value).set_password(password_value).click_login_button()
        return DashboardPage(self._driver)
