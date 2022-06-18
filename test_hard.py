from selene.support.shared import browser
from selene import be, have
# import pytest
# import time #ssssss conflict offsss

def test_hard_form(site_demoqa):
    # browser.open('https://demoqa.com/automation-practice-form')
    # browser.open('https://demoqa.com/automation-practice-form').driver.maximize_window()
    browser.execute_script("var el = document.querySelectorAll('#app > footer'); if (el.length > 0); { el[0].remove(); }")
    browser.element('#firstName').should(be.blank).type('Sam')
    browser.element('#lastName').should(be.blank).type('End')
    browser.element('#userEmail').should(be.blank).type('w@wth.su')
    browser.element('#gender-radio-1')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('88007553535')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="0"]').click()
    browser.element('.react-datepicker__year-select [value="1900"]').click()
    browser.element('.react-datepicker__month .react-datepicker__week .react-datepicker__day--010').click()
    browser.element('#subjectsInput').should(be.blank).set_value('English').press_enter()
    browser.element('#subjectsInput').should(be.blank).set_value('Physics').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture')
    browser.element('#currentAddress').should(be.blank).type('Mou" adress tak daleko chto хочется плакать')
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#city #react-select-4-option-1').click()
    browser.element('#submit').click()
    # time.sleep(5) #Для отладки