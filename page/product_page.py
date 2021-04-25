from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_page import BasePage


class TrendyolProductPage(BasePage):
    """Panel login page https://Trendyol.com """

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.add-to-bs')
    PRODUCT_DETAIL = (By.CSS_SELECTOR, '.pr-in-dt .pr-in-at-tl')

    def __init__(self, driver):
        super().__init__(driver)

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.PRODUCT_DETAIL), "Product page isn't visible!")

    def click_add_to_basket_button(self):
        """
        Clicks add to basket button on product page

        """
        self.wait_for_element(self.ADD_TO_BASKET_BUTTON).click()
