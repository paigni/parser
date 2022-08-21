
from logic import get_urls
from check import is_valid
print('Сборщик ссылок v1.0,перед запуском обратите внимание что вы должны ввести два аргумента'
      ' первый аргумент,ссылка на сам сайт по типу https://pythonworld.ru/ ,второй аргумент глубину погружения по ссылкам')

base_url = input()
pars_depth = input()

def main(a,b):
    if is_valid(b):
        get_urls(b,a)
    else:
        'Неверный ввод'
main(base_url,pars_depth)
