from pages import Chekingattrs

# def test_hidden_layers(browser):
#     ui_main_page = Chekingattrs(browser)
#     ui_main_page.go_to_site()
#     click = ui_main_page.load_hidden_layers()
#     assert True

# def test_load_delay(browser):
#     ui_main_page = Chekingattrs(browser)
#     ui_main_page.go_to_site()
#     click = ui_main_page.loading_pages_section()
#     assert click == 'Success'

# def test_text_input(browser):
#     ui_main_page = Chekingattrs(browser)
#     ui_main_page.go_to_site()
#     text = "sending"
#     click = ui_main_page.load_input(text)
#     assert click == text
#
def test_ajax_data(browser):
    ui_main_page = Chekingattrs(browser)
    ui_main_page.go_to_site()
    click = ui_main_page.load_ajax_request()
    assert True
#
# def test_click(browser):
#     ui_main_page = Chekingattrs(browser)
#     ui_main_page.go_to_site()
#     click = ui_main_page.load_click()
#     assert True
#
# def test_scroll(browser):
#     ui_main_page = Chekingattrs(browser)
#     ui_main_page.go_to_site()
#     click = ui_main_page.load_scrollbars()
#     assert True
#
# def test_dynamic_tables(browser):
#     ui_main_page = Chekingattrs(browser)
#     ui_main_page.go_to_site()
#     click = ui_main_page.load_tables()
#     assert True
