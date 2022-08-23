import sys
from logic import get_urls
from check import is_valid_args, is_valid_arg_2, is_valid_url


def main():
    info = (
        'Сборщик ссылок v1.0,перед запуском обратите внимание что вы должны ввести два аргумента'
        ' первый аргумент,ссылка на сам сайт по типу https://pythonworld.ru/ ,второй '
        'аргумент глубину погружения по ссылкам'
    )
    if len(sys.argv) == 3:
        base_url = sys.argv[1]
        depth = sys.argv[2]
        if is_valid_arg_2(depth):
            if is_valid_args(base_url, int(depth)):
                get_urls(base_url, int(depth))
        else:
            sys.exit('Должно быть число,а не символ')
    if len(sys.argv) == 2:
        base_url = sys.argv[1]
        depth = 3
        if is_valid_url(base_url):
            get_urls(base_url, depth)
        else:
            sys.exit(f'Невалидная ссылка')
    else:
        sys.exit(f"{info}")


if __name__ == '__main__':
    main()
