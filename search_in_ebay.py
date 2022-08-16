# IMPORT RELATED LIBRARIES
import requests
from bs4 import BeautifulSoup

# GET DATA FROM THE URL
def get_data(title):
    url = "https://www.ebay.com/sch/i.html?_nkw=" + title
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

# PARSE DATA AND GET REQUIRED INFOS
def parse(soup):
    productslist = []
    
    results=soup.find_all('li',{'class':'s-item'})
    filter_count = 4
    
    for item in results:
        if (filter_count < 1):
            break
        product = {
            'title': item.find('h3', {'class': 's-item__title'}).text,
            'price': item.find('span', {'class': 's-item__price'}).text,
            'link': item.find('a', {'class': 's-item__link'})['href'],
            'image_src': item.find('img', {'class': 's-item__image-img'})['src']
        }
        if product['title'] != "Shop on eBay":
            productslist.append(product)
        filter_count -= 1
    
    return productslist

# need to give title of the product

"""
soup = get_data("Roku Express | HD Streaming Media Player with High Speed HDMI Cable and Simple Remote")
product_list = parse(soup)

for product in product_list:
    print(product)
"""