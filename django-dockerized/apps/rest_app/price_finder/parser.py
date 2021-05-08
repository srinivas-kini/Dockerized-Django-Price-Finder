from bs4 import BeautifulSoup
import requests
import json
from urllib.parse import quote_plus

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US, en;q=0.5",
}


def get_prices(keyword):
    keyword_ = quote_plus(keyword)
    prices = {}
    prices.update(get_snapdeal_price(keyword_))
    prices.update(get_amazon_price(keyword_))
    return prices


def get_soup(url):
    r = requests.get(url=url, headers=HEADERS)
    return BeautifulSoup(r.text, "lxml")


def get_snapdeal_price(product_name):
    soup = get_soup(
        url=f"https://snapdeal.com/search?keyword={product_name}&noOfResults=1"
    )
    title = soup.find("p", class_="product-title").string
    price = soup.find("span", class_="lfloat product-price").string
    return {"snapdeal": {"price": price, "product": title}}


def get_amazon_price(product_name):

    soup = get_soup(url=f"https://amazon.in/s?k={product_name}")
    try:
        price = soup.find("span", class_="a-price-whole").string
        title = soup.find(
            "span", class_="a-size-base-plus a-color-base a-text-normal"
        ).string
        return {"amazon": {"price": price, "product": title}}
    except (AttributeError, TypeError) as e:
        pass
