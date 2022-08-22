from urllib.parse import urlparse


def check_is_up_url(req):
    if req.status_code == 200:
        return True
    return False


def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def is_valid_arg_2(arg2):
    if arg2.isdigit() and 0 < arg2 < 999:
        return True
    return False


def is_valid_args(arg1, arg2):
    if is_valid_url(arg1):
        if is_valid_arg_2(arg2):
            return True
    return False
