from random import randint
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from base.logger import get_logger


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver, *args, **kwargs):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = get_logger('Page')

    def wait_for_element(self, selector):
        """
        Wait for element to present
        :param selector: locator of the element to find

        """
        return self.wait.until(ec.element_to_be_clickable(selector))

    @staticmethod
    def random_number(first_value, second_value):
        """
        Return random number between parameters
        :param first_value: beginning value of the range
        :param second_value: last value of the range

        """
        return randint(first_value, second_value)

    def presence_of_element_located(self, selector):
        """
        Waits until a element present on the DOM of a page and visible then returns element
        :param selector: Locator of the desired element

        """
        return self.wait.until(ec.presence_of_element_located(selector))
