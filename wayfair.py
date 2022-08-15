from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

def get_data(title):
    url = "https://www.wayfair.com/keyword.php?keyword=" + title
    browser.get(url)
    time.sleep(1)
    
    productslist = []
    
    filter_count = 4
    
    results = browser.find_elements(By.CLASS_NAME, 'pl-ProductCard')
    for i in results:
        if (filter_count < 1):
            break
        productTitle = i.find_element(By.CLASS_NAME, 'pl-ProductCardName')
        productTitle = productTitle.find_element(By.TAG_NAME, 'span').text
        
        # Image sources are secured, so we can't get it right now.
        
        price = i.find_element(By.CLASS_NAME, 'SFPrice')
        price = price.find_element(By.TAG_NAME, 'span').text
        
        product = {
            "title": productTitle,
            "price": price
        }
        
        productslist.append(product)
        filter_count -= 1
        
    browser.quit()
    return productslist


# Get related data by product title    
data = get_data("(2022 Upgrade) AIPER Cordless Robotic Pool Cleaner, Pool Vacuum with Dual-Drive Motors, Self-Parking, Lightweight, Perfect for Above/In-Ground Flat Pools up to 35 Feet (Lasts 50 Mins) - Seagull 600")

print(data)
