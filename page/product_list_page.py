from selenium.webdriver.common.by import By
from base.base_page import BasePage


class TrendyolProductListPage(BasePage):
    """Panel login page https://Trendyol.com """

    PRODUCT = '#boutique-detail-app .boutique-product:nth-child({})'

    def __init__(self, driver):
        super().__init__(driver)

    def select_random_product(self):
        """
        Select random product on product list page

        """
        self.wait_for_element((By.CSS_SELECTOR, self.PRODUCT.format(self.random_number(1, 10)))).click()

    def check_all_product_loaded(self):
        """
            Checks all product are loaded

        """
        return self.driver.find_elements_by_class_name('image-container')

    def check_product_images_loaded(self):
        """
        Checks that the images are loaded after products are loaded, sends a log if they are not
        """

        for product in self.check_all_product_loaded():
            if product.get_attribute('src') != '/Content/images/defaultThumb.jpg':
                self.logger.info('Product images were loaded successfully! ')
            else:
                self.logger.info('Product images were not  loaded successfully! ')
