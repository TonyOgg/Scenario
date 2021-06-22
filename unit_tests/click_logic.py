# from main_logic import Base
# from click_test import TestClick
# from hrefs_and_locators import Hrefs, Locators
# import time
# from selenium.webdriver.common.action_chains import ActionChains as ac
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
#
# class Chekingattrs:
#
#     def load_click(self):
#         search_elem = self.find_link(Hrefs.HREF_CLICK)
#         elem = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(Locators.LOCATOR_NO_CLICK_BUTTON))
#         move_to_element = ac(self.driver).move_to_element(elem).perform()
#         click = self.find_element(Locators.LOCATOR_NO_CLICK_BUTTON)
#         return click

