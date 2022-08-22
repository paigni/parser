from urllib.parse import urlparse
import urllib.request
import urllib.error


def check_is_up_url(url):
    check_is_up = urllib.request.Request(url)
    try:
        urllib.request.urlopen(check_is_up)
        return True
    except urllib.error.URLError:
        return False


def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def is_valid_arg(arg):
    if 0 < arg < 999:
        return True
    return False

# проверка на повтор