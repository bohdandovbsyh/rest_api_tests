import pytest
import json

from framework_from_scratch_parsing.page_objects.login_page import LoginPage
from framework_from_scratch_parsing.utilities.config_parser import ReadConfig
from framework_from_scratch_parsing.utilities.configurations import Configuration
from framework_from_scratch_parsing.utilities.driver_factory import DriverFactory


@pytest.fixture(scope='session')
def env():
    with open(
            '/framework_from_scratch_parsing/configurations/configuration.json') as file:
        env_dict = json.loads(file.read())
    return Configuration(**env_dict)


@pytest.fixture(scope='session')
def create_driver(env):
    driver = DriverFactory.create_driver(driver_id=env.browser_id)
    driver.maximize_window()
    driver.get(env.base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_driver):
    return LoginPage(create_driver)
