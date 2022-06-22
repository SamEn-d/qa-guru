# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__
import pytest
from selene.support.shared import browser
from selene import be, have
# import pytest

def_list = []
site = 'https://demoqa.com/automation-practice-form'


def normal_name(func_name_new):
    if func_name_new == 'open_browser':
        print('Открытие браузера')
    elif func_name_new == 'go_to_companyname_homepage':
        print(f'Переходим на страницу {site}')
    else:
        print(func_name_new.replace('_', ' '))
    # return func_name_new

normal_name("open_browsers")

def open_browser():
    def_list.append(open_browser.__name__)
    normal_name(open_browser.__name__)
    pass

def go_to_companyname_homepage():
    def_list.append(go_to_companyname_homepage.__name__)
    normal_name(go_to_companyname_homepage.__name__)
    pass


def find_registration_button_on_login_page():
    def_list.append(find_registration_button_on_login_page.__name__)
    normal_name(find_registration_button_on_login_page.__name__)
    pass

open_browser()
go_to_companyname_homepage()
find_registration_button_on_login_page()

# print(def_list)
print('________________________')
for i in def_list:
    print(i.replace('_', ' '))
    # print(i)

#Как сделать чтобы было не find_registration_button_on_login_page \ go_to_companyname_homepage \ open_browser
#при normal_name(find_registration_button_on_login_page.__name__)
# А что-то похожее на %s.__name__ ?