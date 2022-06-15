from selene.support.shared import browser
import pytest

def window_size():
    # browser.open('https://google.com')
    browser.driver.set_window_size(width=1920, height=1080)
    #альтернативный вариант
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080

@pytest.fixture(scope='session')
def site_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')
    window_size()

@pytest.fixture
def open_google():
    browser.open('https://google.com')
    # browser.driver.set_window_size(width=1920, height=1080)
    window_size()