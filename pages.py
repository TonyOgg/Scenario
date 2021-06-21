from base import BPage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class Hrefs:
    HREF_HIDDEN_LAYERS = (By.LINK_TEXT, 'Hidden Layers')
    HREF_LOAD_DELAY = (By.LINK_TEXT, 'Load Delay')
    HREF_AJAX_DATA = (By.LINK_TEXT, 'AJAX Data')
    # HREF_CLICK_SIDE_DELAY = (By.LINK_TEXT, 'Client Side Delay')
    HREF_CLICK = (By.LINK_TEXT, 'Click')
    HREF_TEXT_INPUT = (By.LINK_TEXT, 'Text Input')
    HREF_SCROLLBARS = (By.LINK_TEXT, 'Scrollbars')
    HREF_DYNAMIC_TABLE = (By.LINK_TEXT, 'Dynamic Table')


class Locators:
    LOCATOR_BUTTON_HIDDEN_LAYERS = (By.XPATH, "/html//button[@id='greenButton']")
    LOCATOR_BUTTON_LOAD = (By.XPATH, "/html//section//button[@class='btn btn-primary']")
    LOCATOR_AJAX_BUTTON = (By.XPATH, "/html//button[@id='ajaxButton']")
    LOCATOR_AJAX_SUCCESS = (By.XPATH, "//div[@id='content']/p[@class='bg-success']")
    LOCATOR_CLIENT_DELAY_BUTTON = (By.XPATH, "/html//button[@id='ajaxButton']")
    # LOCATOR_CLICK_SIDE_DELAY = (By.XPATH, "//div[@id='content']/p[@class='bg-success']")
    LOCATOR_NO_CLICK_BUTTON = (By.XPATH, "/html//button[@id='badButton']")
    LOCATOR_TEXT_INPUT_FIELD = (By.XPATH, "/html//input[@id='newButtonName']")
    LOCATOR_TEXT_INPUT_BUTTON = (By.XPATH, "/html//button[@id='updatingButton']")
    LOCATOR_SCROLLBARS = (By.XPATH, "/html//section/div/div")
    LOCATOR_BUTTON_IN_SCROLLBAR = (By.XPATH, "/html//button[@id='hidingButton']")
    LOCATOR_DYNAMIC_TABLE_RESULT = (By.XPATH, "/html//section//p[@class='bg-warning']")
    LOCATOR_DYNAMIC_TABLE_ALL = (By.XPATH, "//section//div[@role='table']/div[3]")
    LOCATOR_DYNAMIC_TABLE_HEAD = (By.XPATH, "//section//div[@role='table']/div[2]/div[@role='row']")

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
        search_elem = self.find_link(Hrefs.HREF_AJAX_DATA)
        wait = WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(Locators.LOCATOR_AJAX_BUTTON))
        search_elem = self.find_element(Locators.LOCATOR_AJAX_BUTTON)
        search_elem.click()
        wait = WebDriverWait(self.driver, 16).\
            until(ec.text_to_be_present_in_element(Locators.LOCATOR_AJAX_SUCCESS,
                                                   "Data loaded with AJAX get request."))

        return wait

    # def load_client_side_delay(self):
    #     search_elem = self.find_link(Hrefs.HREF_AJAX_DATA)
    #     search_elem = self.find_element(Locators.LOCATOR_AJAX_BUTTON)
    #     search_elem.click()
    #     wait = WebDriverWait(self.driver, 16).\
    #         until(ec.text_to_be_present_in_element(Locators.LOCATOR_AJAX_SUCCESS,
    #                                                "Data loaded with AJAX get request."))
    #     return wait

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
        search_elem.send_keys(text)
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






