from lib.pages import AdminLoginPage, AdminLayout
import lib.misc.variables as v
import pytest
import allure


@allure.title("Admin successful and failed logins")
@allure.feature("Admin successful and failed logins")
@allure.tag("Admin")
@pytest.mark.admin
class TestAdminLogin:
    @allure.title("Admin successfully logs in")
    @allure.description("Admin is on the login page\n"
                        "Admin logs in with a valid username and a valid password\n"
                        "Admin is logged in")
    @allure.testcase("TC-1")
    def test_admin_successful_login(self, browser):
        # Admin is on the login page
        page = AdminLoginPage(browser)
        page.visit()
        page.banner_button.click()

        # Admin logs in with a valid username and a valid password
        page.login(v.ADMIN_USERNAME, v.ADMIN_PASSWORD)

        # Admin is logged in
        page = AdminLayout(browser)
        assert page.logout_button

    @allure.title("Admin attempts to log in with an invalid password")
    @allure.description("Admin is on the login page\n"
                        "Admin attempts to log in with a valid username and an invalid password\n"
                        "Admin sees validation markings in the login form\n"
                        "Admin is not logged in")
    @allure.testcase("TC-2")
    def test_admin_invalid_login_password(self, browser):
        # Admin is on the login page
        page = AdminLoginPage(browser)
        page.visit()
        page.banner_button.click()

        # Admin attempts to log in with a valid username and an invalid password
        page.login(v.ADMIN_USERNAME, v.ADMIN_INVALID_PASSWORD)

        # Admin sees validation markings in the login form
        assert page.username_validation_border
        assert page.password_validation_border

        # Admin is not logged in
        assert page.username_field
        assert page.password_field
        assert page.login_button
