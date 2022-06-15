from selene.support.shared import browser
import pytest

def window_size():
    # browser.open('https://google.com')
    browser.driver.set_window_size(width=1920, height=1080)

@pytest.fixture(scope='session')
def site_demoqa():
    browser.open('https://demoqa.com/automation-practice-form')
    window_size()

@pytest.fixture
def open_google():
    browser.open('https://google.com')
    # browser.driver.set_window_size(width=1920, height=1080)
    window_size()


    # browser.driver.set_window_size(width=1920, height=1080)
# from selene.support.shared import browser
# import pytest
#
#
# @pytest.fixture(scope='session', autouse=True)
# def setup():
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#
#


# from selene.support.shared import browser
# import pytest
#
# @pytest.fixture(scope='session', autouse=True)
# def window_size():
#     # browser.open('data:')
#     browser.driver.set_window_size(width=1920, height=1080)
#
# @pytest.fixture
# def site_google():
#     browser.open('https://google.com')
#
# @pytest.fixture
# def site_demoqa():
#     browser.open('https://demoqa.com/automation-practice-form')