# IMPORT RELATED LIBRARIES
import requests
from bs4 import BeautifulSoup

def get_data_google(title):
    url = "https://www.google.com/search?q=" + title +"&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsANKBAhBGABKBAhGGABQzQJYzQJg8QdoAXABeACAAQCIAQCSAQCYAQCgAQKgAQHIAQjAAQE&sclient=gws-wiz"
    
    productslist = []
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    
    results=soup.find_all('div',{'class':'Gx5Zad'})
    
    for item in results:
        try:
            store = item.find('div', {'class' : 'UPmit'}).get_text()
            store = store.split("com")[0] + 'com'
        except:
            store = "No Store"
            
        try:
            title = item.find('div', {'class' : 'vvjwJb'}).get_text()
        except:
            title = "No Title"
            
        price= "No Price"
        try:
            price_list = item.findAll('span', {'class': 'r0bn4c'})
            for i in price_list:
                s = i.get_text()
                if ("$" in s):
                    price = s
        except:
            price = "No Price"
            
        try:
            link = item.find('div', {'class': 'egMi0'}).find('a')['href']
            link = link.split("q=")[1].split('&')[0]
        except:
            link = "No Link"
            
        if (title != "" and title != "No Title" and link != "No Link"):
        
            product = {
                'title': title,
                'price': price,
                'link': link,
                'store': store 
            }
            productslist.append(product)
                
        
    
    return productslist
"""
data = get_data_google("Roku Express 4K+ 2021 | Streaming Media Player HD/4K/HDR with Smooth Wireless Streaming and Roku Voice Remote with TV Controls, Includes Premium HDMI® Cable")
print(data)
"""