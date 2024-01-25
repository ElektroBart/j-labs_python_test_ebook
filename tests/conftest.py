import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
