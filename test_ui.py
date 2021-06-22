import pytest
from pages import Chekingattrs


class TestMyFunctions:

    def test_click(self, browser):
        ui_main_page = Chekingattrs(browser)
        ui_main_page.go_to_site()
        click = ui_main_page.load_click()
        assert True

    def test_scroll(self, browser):
        ui_main_page = Chekingattrs(browser)
        ui_main_page.go_to_site()
        click = ui_main_page.load_scrollbars()
        assert True

    def test_dynamic_tables(self, browser):
        ui_main_page = Chekingattrs(browser)
        ui_main_page.go_to_site()
        click = ui_main_page.load_tables()
        assert True

    def test_hidden_layers(self, browser):
        ui_main_page = Chekingattrs(browser)
        ui_main_page.go_to_site()
        click = ui_main_page.load_hidden_layers()
        assert True

    def test_load_delay(self, browser):
        ui_main_page = Chekingattrs(browser)
        ui_main_page.go_to_site()
        click = ui_main_page.loading_pages_section()
        assert click == 'Success'

    def test_text_input(self, browser):
        ui_main_page = Chekingattrs(browser)
        ui_main_page.go_to_site()
        text = "sending"
        click = ui_main_page.load_input(text)
        assert click == text

    def test_ajax_data(self, browser):
        ui_main_page = Chekingattrs(browser)
        ui_main_page.go_to_site()
        click = ui_main_page.load_ajax_request()
        assert True

    def test_client_side_delay(self, browser):
        ui_main_page = Chekingattrs(browser)
        ui_main_page.go_to_site()
        click = ui_main_page.load_client_side_delay()
        assert True

    def test_verify_text(self, browser):
        ui_main_page = Chekingattrs(browser)
        ui_main_page.go_to_site()
        text = "Welcome"
        search = ui_main_page.search_verify_text(text)
        assert text == search

    def test_progress_bar(self, browser):
        ui_main_page = Chekingattrs(browser)
        ui_main_page.go_to_site()
        percent = '75'
        check = ui_main_page.checking_percent(percent)
        assert float(percent) == pytest.approx(check, 0.1)
