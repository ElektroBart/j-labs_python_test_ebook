from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.products_page import ProductsPage

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.login_logo_locator = (By.CLASS_NAME, "login_logo")
        self.username_input_locator = (By.ID, "user-name")
        self.password_input_locator = (By.ID, "password")
        self.login_button_locator = (By.ID, "login-button")
        self.error_message_locator = (By.CLASS_NAME, "error-message-container")

    def open_login_page(self):
        self.browser.get("https://www.saucedemo.com")
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.login_logo_locator))

    def enter_username(self, username):
        username_input = self.browser.find_element(*self.username_input_locator)
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.browser.find_element(*self.password_input_locator)
        password_input.clear()
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self.browser.find_element(*self.login_button_locator)
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return ProductsPage(self.browser)

    def get_error_message_text(self):
        WebDriverWait(self.browser, 1).until(EC.presence_of_element_located(self.error_message_locator))
        error_message_element = self.browser.find_element(*self.error_message_locator)
        return error_message_element.text
