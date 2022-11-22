import pytest
from selenium.webdriver.support.wait import WebDriverWait

from framework_from_scratch.page_objects.login_page import LoginPage
from framework_from_scratch.utilities.config_parser import ReadConfig
from framework_from_scratch.utilities.driver_factory import DriverFactory


@pytest.fixture(scope='session')
def create_driver():
    driver = DriverFactory.create_driver(driver_id=ReadConfig.get_driver_id())
    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)
