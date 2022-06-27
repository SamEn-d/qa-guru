# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def_list = []

def def_name_and_args (func_args):
    # Узнать имя функции
    name = func_args.__name__.replace('_', ' ')
    print(f'Функция: {name}')
    s = 0
    for i in func_args.__code__.co_varnames:
        s += 1
        i = i.replace('_', ' ')
        print(f'Аргумент {s}: {i}')
    print('____END____')

def open_browser(browser_name):
    pass

def go_to_companyname_homepage(page_url):
    pass

def find_registration_button_on_login_page(page_url, button_text):
    pass


print(def_list)
functions = (open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)
for n in functions:
    def_name_and_args (n)