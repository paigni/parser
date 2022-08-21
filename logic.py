import requests
from check import is_valid
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import argparse
base_url = 'https://pythonworld.ru/'
def get_urls(url,depth=3):
    urls = set()
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        urls.add(href)
    urls = list(urls)
    if depth > 0:
        for link in urls:
            g = '   '
            get_urls(link, depth - 1)
            print(g * depth + link)
        return urls
get_urls(base_url)


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='?')
    parser.add_argument('parsing_depth',default=3)
    return parser