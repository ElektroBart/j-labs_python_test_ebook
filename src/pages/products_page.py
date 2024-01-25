from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_title_locator = (By.CLASS_NAME, 'title')

    def get_products_title(self):
        products_title = self.driver.find_element(*self.products_title_locator)
        return products_title.text

    def is_products_page_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.products_title_locator)
            )
            return True
        except Exception as e:
            return False