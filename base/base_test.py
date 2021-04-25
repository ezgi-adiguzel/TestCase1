import unittest
from pathlib import Path
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from base.logger import get_logger


class TestBaseWeb(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        options = Options()
        ROOT_DIR = Path(__file__).parent.parent
        driver_path = ROOT_DIR / 'webDrivers/'
        self.driver = webdriver.Chrome(str(driver_path) + '/chromedriverLinux64', options=options)
        self.driver.maximize_window()
        self.logger = get_logger(self._testMethodName)
