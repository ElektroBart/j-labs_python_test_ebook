from src.pages.login_page import LoginPage


class TestLoginPage:
    correct_username = "standard_user"
    correct_password = "secret_sauce"

    def test_successful_login(self, browser):
        login_page = LoginPage(browser)
        login_page.open_login_page()
        products_page = login_page.login(self.correct_username, self.correct_password)
        products_page.is_products_page_loaded()
        assert products_page.get_products_title() == "Products", "Page title doesn't match"

    def test_empty_username_and_password(self, browser):
        login_page = LoginPage(browser)
        login_page.open_login_page()
        login_page.click_login_button()
        assert login_page.get_error_message_text() == "Username and password are required", \
            "The error message doesn't match."

    def test_empty_username(self, browser):
        login_page = LoginPage(browser)
        login_page.open_login_page()
        login_page.enter_password(self.correct_password)
        login_page.click_login_button()
        assert login_page.get_error_message_text() == "Username is required", \
            "The error message doesn't match."

    def test_empty_password(self, browser):
        login_page = LoginPage(browser)
        login_page.open_login_page()
        login_page.enter_username(self.correct_username)
        login_page.click_login_button()
        assert login_page.get_error_message_text() == "Password is required", \
            "The error message doesn't match."
