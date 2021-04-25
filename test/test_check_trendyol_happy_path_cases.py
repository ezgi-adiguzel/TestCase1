from page.login_page import TrendyolLoginPage
from page.main_page import TrendyolMainPage
from page.butique_page import TrendyolButiquePage
from page.product_page import TrendyolProductPage
from page.product_list_page import TrendyolProductListPage
from base.base_test import *
import time
import unittest


class TestCheckTrendyolHappyPathCases(TestBaseWeb):
    """Test case is:

      1. Log in the Trendyol
      2. Click on the category tabs to check the image send log if there is an unloaded image
      3. Select random boutique, upload your product images and check that it is not loaded, if there is an error, send a log
      4. Select random product and go to product details page
      5. Add product to cart

      """
    email = ''
    password = ''
    web_site_url = 'http://www.trendyol.com'
    categories_tab_name = ['KADIN', 'ERKEK', 'ÇOCUK', 'EV & YAŞAM', 'SÜPERMARKET', 'KOZMETİK', 'AYAKKABI & ÇANTA',
                  'SAAT & AKSESUAR', 'ELEKTRONİK']

    def setUp(self):
        self.driver.get(self.web_site_url)

    def test_check_trendyol_happy_path_cases(self):
        """ Test checks Customer Trendyol Happy Path cases """

        self.logger.info("1. Log in the Trendyol")
        time.sleep(1)
        self.main_page = TrendyolMainPage(self.driver)
        self.main_page.click_close_btn_on_popup()
        self.main_page.click_sign_in_item()
        self.login_page = TrendyolLoginPage(self.driver)
        self.login_page.fill_login_form(self.email, self.password)
        self.login_page.click_log_in_btn()
        time.sleep(1)
        self.assertEqual(self.main_page.is_my_account_item_present(), 'Hesabım',
                         "user could not login successfully!")
        self.logger.info("User was able to login successfully!")

        self.logger.info("2. Click on the category tabs to check the image send log if there is an unloaded image")
        self.butique_page = TrendyolButiquePage(self.driver)
        for category_tab_name in self.categories_tab_name:
            self.main_page.click_category_tab(category_tab_name)
            self.butique_page.check_butique_images_loaded(category_tab_name)
            self.logger.info("{} loaded on category tabs successfully!".format(category_tab_name))
        self.logger.info("All images were loaded on category tabs successfully!")

        self.logger.info("3. Select random boutique, upload your product images and check that it is not loaded, "
                         "if there is an error, send a log")
        self.butique_page.select_random_butique()
        self.butique_page.check_butique_images_loaded('Random Butique')
        self.logger.info("All images were uploaded on butiques successfully!")

        self.logger.info("4. Select random product and go to product details page")
        self.product_list_page = TrendyolProductListPage(self.driver)
        self.product_list_page.check_product_images_loaded()
        self.product_list_page.select_random_product()
        self.logger.info("Check product list images and Product was selected successfully!")

        self.logger.info("5. Add product to cart")
        self.product_page = TrendyolProductPage(self.driver)
        self.product_page.click_add_to_basket_button()
        self.logger.info("Product was added on cart page successfully!")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
