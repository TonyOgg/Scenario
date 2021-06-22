from base import BPage
from hrefs_and_locators import Hrefs, Locators
import time
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



class Chekingattrs(BPage):

    def load_hidden_layers(self):
        search_elem = self.find_link(Hrefs.HREF_HIDDEN_LAYERS)
        search_elem = self.find_element(Locators.LOCATOR_BUTTON_HIDDEN_LAYERS).click()
        if self.find_element(Locators.LOCATOR_BUTTON_HIDDEN_LAYERS) is False:
            return True

    def loading_pages_section(self):
        search_elem = self.find_link(Hrefs.HREF_LOAD_DELAY)
        search_elem = ec.visibility_of_element_located(Hrefs.HREF_LOAD_DELAY)
        search_elem = self.find_element(Locators.LOCATOR_BUTTON_LOAD)
        try:
            search_elem.click()
        except Exception as e:
            'No_click'
        return 'Success'

    def load_ajax_request(self):
        link_to_page = self.find_link(Hrefs.HREF_AJAX_DATA)
        wait = WebDriverWait(self.driver, 6).until(ec.visibility_of_element_located(Locators.LOCATOR_AJAX_BUTTON))
        search_elem = self.find_element(Locators.LOCATOR_AJAX_BUTTON)
        time.sleep(1)
        search_elem.click()
        wait = WebDriverWait(self.driver, 16).\
            until(ec.visibility_of_element_located(Locators.LOCATOR_AJAX_SUCCESS))
        time.sleep(1)
        search_elem.click()
        wait = WebDriverWait(self.driver, 16). \
            until(ec.presence_of_all_elements_located(Locators.LOCATOR_AJAX_LOAD))
        return wait

    def search_verify_text(self, text):
        link_to_page = self.find_link(Hrefs.HREF_VERIFY_TEXT)
        hole_elem = self.find_element(Locators.LOCATOR_VERIFY_TEXT).text
        user_elem = self.find_element(Locators.LOCATOR_VERIFY_TEXT_USERNAME).text
        searching_element = hole_elem.split(' ' + user_elem)[0]
        return searching_element

    def checking_percent(self, percent):
        link_to_page = self.find_link(Hrefs.HREF_PROGRESS_BAR)
        w = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(Locators.LOCATOR_START_PROGRESS_BAR))
        start = self.find_element(Locators.LOCATOR_START_PROGRESS_BAR)
        time.sleep(1)
        start.click()
        LOCATOR_STATUS_PROGRESS_BAR = (By.XPATH, "/html//div[@id='progressBar' and @aria-valuenow={0}]".format(percent))
        wait = WebDriverWait(self.driver, 100).until(ec.presence_of_element_located
                                                   (LOCATOR_STATUS_PROGRESS_BAR))
        stop = self.find_element(Locators.LOCATOR_STOP_PROGRESS_BAR)
        stop.click()
        return float(wait.text[:-1])

    def load_client_side_delay(self):
        link_to_page = self.find_link(Hrefs.HREF_CLIENT_SIDE_DELAY)
        wait = WebDriverWait(self.driver, 6).until(ec.visibility_of_element_located
                                                   (Locators.LOCATOR_CLICK_CLIENT_SIDE_DELAY))
        search_elem = self.find_element(Locators.LOCATOR_CLICK_CLIENT_SIDE_DELAY)
        time.sleep(1)
        search_elem.click()
        wait = WebDriverWait(self.driver, 16). \
            until(ec.visibility_of_element_located(Locators.LOCATOR_CLICK_CLIENT_SIDE_DELAY_SUCCESS))
        time.sleep(1)
        search_elem.click()
        wait = WebDriverWait(self.driver, 16). \
            until(ec.presence_of_all_elements_located(Locators.LOCATOR_CLICK_CLIENT_SIDE_DELAY_LOAD))
        return wait

    def load_click(self):
        search_elem = self.find_link(Hrefs.HREF_CLICK)
        elem = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(Locators.LOCATOR_NO_CLICK_BUTTON))
        move_to_element = ac(self.driver).move_to_element(elem).perform()
        click = self.find_element(Locators.LOCATOR_NO_CLICK_BUTTON)
        return click

    def load_input(self, text):
        search_elem = self.find_link(Hrefs.HREF_TEXT_INPUT)
        search_elem = self.find_element(Locators.LOCATOR_TEXT_INPUT_FIELD)
        search_elem.clear()
        time.sleep(1)
        search_elem.send_keys(text)
        time.sleep(1)
        click_button = self.find_element(Locators.LOCATOR_TEXT_INPUT_BUTTON)
        time.sleep(1)
        click_button.click()
        return click_button.text

    def load_scrollbars(self):
        search_elem = self.find_link(Hrefs.HREF_SCROLLBARS)
        search_elem = self.find_element(Locators.LOCATOR_SCROLLBARS)
        f_loc = self.find_element(Locators.LOCATOR_BUTTON_IN_SCROLLBAR)
        elem = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(Locators.LOCATOR_SCROLLBARS))
        el = ac(self.driver).move_to_element(f_loc).perform()
        self.driver.implicitly_wait(3)
        search_elem = self.find_element(Locators.LOCATOR_BUTTON_LOAD).click()
        return search_elem

    def load_tables(self):
        search_elem = self.find_link(Hrefs.HREF_DYNAMIC_TABLE)
        search_elem = self.find_element(Locators.LOCATOR_DYNAMIC_TABLE_RESULT)
        f_param = search_elem.text.split(' ')[0]
        s_param = search_elem.text.split(' ')[1][:-1]
        t_param = search_elem.text.split(' ')[2]
        namegr = self.find_element(Locators.LOCATOR_DYNAMIC_TABLE_HEAD).text.split(' ')
        rowgr = self.find_element(Locators.LOCATOR_DYNAMIC_TABLE_ALL).text
        param = rowgr.split(f_param)[1].split('%')[0].split(' ')[-1]
        return t_param == param






