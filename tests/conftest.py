import pytest
from selenium import webdriver
from src.pages.login_page import LoginPage


@pytest.fixture(scope='class')
def browser(request):
    browser = request.config.getoption("--browser")
    print(browser)
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name: chrome, firefor or edge")


@pytest.fixture
def login_page(browser):
    log_page = LoginPage(browser)
    log_page.open_login_page()
    return log_page
