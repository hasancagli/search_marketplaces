from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

def get_data_google(title):
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
            
        if (title != "" and title != "No Title" and link != "No Link"):
        
            product = {
                'title': title,
                'price': price, 
                'link': link,
                'store': store 
            }
            productslist.append(product)
    
    browser.quit()
    return productslist
""" 
data = get_data_google("Roku Express 4K+ 2021 | Streaming Media Player HD/4K/HDR with Smooth Wireless Streaming and Roku Voice Remote with TV Controls, Includes Premium HDMI® Cable")
print(data)
browser.quit()
"""