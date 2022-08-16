from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

def get_data(title):
    browser.get("https://www.google.com/search?q=" + title +"&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsANKBAhBGABKBAhGGABQzQJYzQJg8QdoAXABeACAAQCIAQCSAQCYAQCgAQKgAQHIAQjAAQE&sclient=gws-wiz")
    
    productslist = []
    
    results = browser.find_elements(By.CLASS_NAME, 'MjjYud')
    
    for item in results:
    
        try:
            store = item.find_element(By.CLASS_NAME, 'iUh30').text
            store = store.split("com")[0] + 'com'
        except:
            store = "No Store"
        
        try:
            title = item.find_element(By.CLASS_NAME, 'LC20lb').text
        except:
            title = "No Title"
        
        price= "No Price"
        try:
            price_list = item.find_element(By.CLASS_NAME, 'fG8Fp').find_elements(By.TAG_NAME, 'span')
            for i in price_list:
                s = i.text
                if ("$" in s):
                    price = s
        except:
            price = "No Price"
            
        try:
            link = item.find_element(By.CLASS_NAME, 'yuRUbf').find_element(By.TAG_NAME, 'a').get_attribute('href')
        except:
            link = "No Link"
            
        if (title != "" and title != "No Title" and price != "No Price"):
        
            product = {
                'title': title,
                'price': price, 
                'link': link,
                'store': store 
            }
            productslist.append(product)
    
    return productslist
    
data = get_data("2021 Apple 10.2-inch iPad (Wi-Fi, 64GB) - Silver")
print(data)