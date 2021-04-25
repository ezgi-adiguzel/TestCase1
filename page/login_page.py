from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class TrendyolLoginPage(BasePage):
    """Trendyol login page  https://Trendyol.com """

    EMAIL_INPUT = (By.ID, 'login-email')
    PASSWORD_INPUT = (By.ID, 'login-password-input')
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".q-button.submit")

    def __init__(self, driver):
        super().__init__(driver)
        self.check()

    def check(self):
        self.wait.until(ec.visibility_of_element_located(self.EMAIL_INPUT), "Login page isn't visible!")
        self.wait.until(ec.visibility_of_element_located(self.PASSWORD_INPUT), "Login page isn't visible!")
        self.wait.until(ec.visibility_of_element_located(self.SIGN_IN_BUTTON), "Login page isn't visible!")

    def fill_login_form(self, email, password):
        """
        Fills email and password inputs in login form
        :param str email: String value that is used as login of Trendyol account
        :param str password: String value that is used as password of Trendyol account

        """
        self.wait_for_element(self.EMAIL_INPUT).send_keys(email)
        self.wait_for_element(self.PASSWORD_INPUT).send_keys(password)

    def click_log_in_btn(self):
        """
        Submits log in and returns Trendyol Main Page

        """
        self.wait_for_element(self.SIGN_IN_BUTTON).click()
