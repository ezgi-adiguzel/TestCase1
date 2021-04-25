from selenium.webdriver.common.by import By
from base.base_page import BasePage


class TrendyolMainPage(BasePage):
    """Panel login page https://Trendyol.com """

    CATEGORY_NAME = './/*[contains(@class, "category-header") and contains(text(), "{}")]'
    POP_UP_CLOSE_BTN = (By.ID, 'Combined-Shape')
    SIGN_IN_ITEM = (By.CLASS_NAME, 'user-login-container')
    CLOSE_BTN = (By.ID, "Combined-Shape")
    MY_ACCOUNT_ITEM = (By.CSS_SELECTOR, '.account-user')

    def __init__(self, driver):
        super().__init__(driver)

    def click_category_tab(self, category_tab_name):
        """
        clicks 'KADIN', 'ERKEK', 'ÇOCUK', 'EV & YAŞAM', 'SÜPERMARKET', 'KOZMETİK', 'AYAKKABI & ÇANTA',
                  'SAAT & AKSESUAR', 'ELEKTRONİK' C

        """
        self.wait_for_element((By.XPATH, self.CATEGORY_NAME.format(category_tab_name))).click()

    def click_sign_in_item(self):
        """
        Clicks Sign In item on Trendyol Main Page

        """
        self.wait_for_element(self.SIGN_IN_ITEM).click()

    def click_close_btn_on_popup(self):
        """
        Clicks close button If popup appears before login

        """
        try:
            self.wait_for_element(self.CLOSE_BTN).click()
            self.logger.info('Popup is closed successfully!')
        except:
            self.logger.info('Popup is not closed successfully!')

    def is_my_account_item_present(self):
        """
        Check my account items 'Hesabım' after login

        """
        return self.wait_for_element(self.MY_ACCOUNT_ITEM).text
