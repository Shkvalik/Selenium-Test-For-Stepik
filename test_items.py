import time


def test_change_user_language(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(5)  # Сократил время на проверку, чтобы не занимать время
    active_button = browser.find_element_by_css_selector("button[class='btn btn-lg btn-primary btn-add-to-basket']")
    assert active_button, print('Button is not found')
    print('Hi')

# Pytest command
# pytest --language=fr test_items.py
# pytest --language=eu test_items.py
# pytest --language=ru test_items.py
