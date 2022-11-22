import pytest


@pytest.mark.first_test
def test_01(open_login_page):
    login_page = open_login_page
    dashboard_page = login_page.login('admin@yourstore.com', 'admin')
    assert dashboard_page.is_logout_button_displayed() is True, 'User was not logged-in'
