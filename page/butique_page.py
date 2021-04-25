import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage


class TrendyolButiquePage(BasePage):
    """Trendyol Butique page https://www.trendyol.com/butik/liste  """

    BUTIQUE = '.component-list .component-item:nth-child({})'

    def __init__(self, driver):
        super().__init__(driver)

    def select_random_butique(self):
        """
       Select  butique on butique pages

        """
        self.wait_for_element((By.CSS_SELECTOR, self.BUTIQUE.format(self.random_number(1, 15)))).click()

    def check_all_butiques_loaded(self):
        """
        Checks all butiques are loaded

        """
        time.sleep(1)
        return self.driver.find_elements_by_class_name('image-container img')

    def check_butique_images_loaded(self, category):
        """
        Checks that the images are loaded after boutiques are loaded, sends a log if they are not
        """

        for butique in self.check_all_butiques_loaded():
            if butique.get_attribute('src') != 'https://cdn.dsmcdn.com/web/production/large_boutique_placeholder.png':
                self.logger.info('{} images were loaded successfully!'.format(category))
            else:
                self.logger.info('{} images were not loaded successfully!'.format(category))
