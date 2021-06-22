import time
import unittest
from selenium import webdriver
from main_logic import Base
# from click_logic import Chekingattrs
from selectors_and_locators import Selectors, Locators


class TestClick(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../venv/lib/python3.9/site-packages/selenium/webdriver/chrome/chromedriver')
        self.driver.maximize_window()
        self.base_url = "http://uitestingplayground.com/"

    def test_click_func(self):
        self.driver.get(self.base_url)
        elem = Base()
        elem.click_link(self.driver, Selectors.CSS_CLICK_NAME)
            # driver.find_element_by_css_selector(Selectors.CSS_CLICK_NAME)
        page = elem.click()
        time.sleep(10)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
