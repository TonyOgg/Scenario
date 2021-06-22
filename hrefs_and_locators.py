from selenium.webdriver.common.by import By


class Hrefs:
    HREF_HIDDEN_LAYERS = (By.LINK_TEXT, 'Hidden Layers')
    HREF_LOAD_DELAY = (By.LINK_TEXT, 'Load Delay')
    HREF_AJAX_DATA = (By.LINK_TEXT, 'AJAX Data')
    HREF_CLIENT_SIDE_DELAY = (By.LINK_TEXT, 'Client Side Delay')
    HREF_CLICK = (By.LINK_TEXT, 'Click')
    HREF_TEXT_INPUT = (By.LINK_TEXT, 'Text Input')
    HREF_SCROLLBARS = (By.LINK_TEXT, 'Scrollbars')
    HREF_DYNAMIC_TABLE = (By.LINK_TEXT, 'Dynamic Table')
    HREF_VERIFY_TEXT = (By.LINK_TEXT, 'Verify Text')
    HREF_PROGRESS_BAR = (By.LINK_TEXT, 'Progress Bar')


class Locators:
    LOCATOR_BUTTON_HIDDEN_LAYERS = (By.XPATH, "/html//button[@id='greenButton']")
    LOCATOR_BUTTON_LOAD = (By.XPATH, "/html//section//button[@class='btn btn-primary']")
    LOCATOR_AJAX_BUTTON = (By.XPATH, "/html//button[@id='ajaxButton']")
    LOCATOR_AJAX_SUCCESS = (By.XPATH, "//div[@id='content']/p[@class='bg-success']")
    LOCATOR_AJAX_LOAD = (By.XPATH, "/html//i[@id='spinner']")
    LOCATOR_CLICK_CLIENT_SIDE_DELAY = (By.XPATH, "/html//button[@id='ajaxButton']")
    LOCATOR_CLICK_CLIENT_SIDE_DELAY_SUCCESS = (By.XPATH, "//div[@id='content']/p[1]")
    LOCATOR_CLICK_CLIENT_SIDE_DELAY_LOAD = (By.XPATH, "/html//i[@id='spinner']")
    LOCATOR_NO_CLICK_BUTTON = (By.XPATH, "/html//button[@id='badButton']")
    LOCATOR_TEXT_INPUT_FIELD = (By.XPATH, "/html//input[@id='newButtonName']")
    LOCATOR_TEXT_INPUT_BUTTON = (By.XPATH, "/html//button[@id='updatingButton']")
    LOCATOR_SCROLLBARS = (By.XPATH, "/html//section/div/div")
    LOCATOR_BUTTON_IN_SCROLLBAR = (By.XPATH, "/html//button[@id='hidingButton']")
    LOCATOR_DYNAMIC_TABLE_RESULT = (By.XPATH, "/html//section//p[@class='bg-warning']")
    LOCATOR_DYNAMIC_TABLE_ALL = (By.XPATH, "//section//div[@role='table']/div[3]")
    LOCATOR_DYNAMIC_TABLE_HEAD = (By.XPATH, "//section//div[@role='table']/div[2]/div[@role='row']")
    LOCATOR_VERIFY_TEXT = (By.XPATH,
                           "/html//section//div[@class='bg-primary']/span[@class='badge-secondary']")
    LOCATOR_VERIFY_TEXT_USERNAME = (By.XPATH,
                    "/html//section//div[@class='bg-primary']/span[@class='badge-secondary']/span[.='UserName']")
    LOCATOR_START_PROGRESS_BAR = (By.XPATH, "/html//button[@id='startButton']")
    LOCATOR_STOP_PROGRESS_BAR = (By.XPATH, "/html//button[@id='stopButton']")

