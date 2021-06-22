from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://uitestingplayground.com/"

    def find_element(self, locator, time=7):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_link(self, link, time=7):
        elem = WebDriverWait(self.driver, time).until(ec.presence_of_element_located(link),
                                                      message=f"Can't find element by link {link}")
        elem.click()
        return elem

    def go_to_site(self):
        return self.driver.get(self.base_url)


