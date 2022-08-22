import sys
from logic import get_urls
from check import is_valid_url,is_valid_arg,check_is_up_url
print('Сборщик ссылок v1.0,перед запуском обратите внимание что вы должны ввести два аргумента'
      ' первый аргумент,ссылка на сам сайт по типу https://pythonworld.ru/ ,второй аргумент глубину погружения по ссылкам')


def main():
    base_url = sys.argv[1]
    depth = int(sys.argv[2])
    check_to_valid = is_valid_url(base_url)
    check_is_up = check_is_up_url(base_url)
    if check_to_valid and check_is_up:
        if is_valid_arg(depth):
            get_urls(base_url, depth)
    else:
        input('Неверный ввод')


if __name__ == '__main__':
        main()