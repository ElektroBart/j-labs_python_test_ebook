import pytest
from selenium import webdriver
from src.pages.login_page import LoginPage


@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login_page(browser):
    log_page = LoginPage(browser)
    log_page.open_login_page()
    return log_page
