from selene.support.shared import browser
from selene import be, have

google_search_text = 'selene'
google_search_results = 'Селена - Википедия'
google_search_results_broken = 'Всё херня, переделывай'
google_search_results_no_result = 'lksfgbjhopi kdf msvoniguidxf,viugapoivdsjzm fizwepsidz'

def test_one(open_google):
    # browser.open('https://google.com')
    # browser.driver.set_window_size(width=1920, height=1080)
    browser.element('[name="q"]').should(be.blank).type(google_search_text).press_enter()
    browser.element('[id="search"]').should(have.text(google_search_results))

def test_one_broken(open_google):
    # browser.open('https://google.com')
    # browser.driver.set_window_size(width=1920, height=1080)
    browser.element('[name="q"]').should(be.blank).type(google_search_text).press_enter()
    browser.element('[id="search"]').should(have.text(google_search_results_broken))

def test_one_no_result(open_google):
    # browser.open('https://google.com')
    # browser.driver.set_window_size(width=1920, height=1080)
    browser.element('[name="q"]').should(be.blank).type(google_search_results_no_result).press_enter()
    browser.element('[id="rcnt"]').should(have.text(google_search_results_no_result))

