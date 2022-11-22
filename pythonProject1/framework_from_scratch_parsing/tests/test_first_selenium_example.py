import pytest


@pytest.mark.first_test
def test_01(open_login_page, env):
    login_page = open_login_page
    dashboard_page = login_page.login(env.user_name, env.password)
    assert dashboard_page.is_logout_button_displayed() is True, 'User was not logged-in'
