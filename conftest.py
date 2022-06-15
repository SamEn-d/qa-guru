import pytest

@pytest.fixture(scope='session', autouse=True)
def window_size():
    browser.open('data:')
    browser.driver.set_window_size(width=1920, height=1080)