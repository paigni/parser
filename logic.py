import requests
from check import is_valid_url, check_is_up_url
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_urls(url, depth, counter=0):
    urls = set()
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    tags = soup.findAll('a')

    for tag in tags:
        href = tag.attrs.get("href")
        if href == "" or href is None:
            continue
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid_url(href):
            continue
        if not check_is_up_url(req):
            continue
        urls.add(href)

    urls = list(urls)
    if depth > 0:
        for url in urls:
            space = '\t'
            get_urls(url, depth-1, counter+1)
            print(space * counter + url)
        return urls
