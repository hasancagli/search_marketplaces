from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

def get_data(title):

    url = "https://www.walmart.com/search?q=" + title
    browser.get(url)
    time.sleep(20)

    productsList = []
    
    results = browser.find_elements(By.CLASS_NAME, 'list-view')
    print(len(results))
    
    browser.quit()
    return productsList
    
# Get related data by product title    
data = get_data("(2022 Upgrade) AIPER Cordless Robotic Pool Cleaner, Pool Vacuum with Dual-Drive Motors, Self-Parking, Lightweight, Perfect for Above/In-Ground Flat Pools up to 35 Feet (Lasts 50 Mins) - Seagull 600")

print(data)