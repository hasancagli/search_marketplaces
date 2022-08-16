from bs4 import BeautifulSoup
import requests
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# IMPORT FUNCTIONS
from search_different_marketplaces_amazon import get_price, execute_get_price, run_program
from search_in_ebay import get_data, parse
from search_in_google_bs4 import get_data_google

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

amazon_dict = {
    "amazon.com": "United States",
    "amazon.ca": "Canada",
    "amazon.com.mx": "Mexico",
    "amazon.com.br" : "Brazil",
    "amazon.ae": "United Arab Emirates",
    "amazon.com.tr":"Turkey",
    "amazon.jp": "Japan",
    "amazon.com.au": "Australia",
    "amazon.sg": "Singapore",
    "amazon.in":"India",
    "amazon.de":"Germany",
    "amazon.co.uk":"United Kingdom",
    "amazon.fr":"France",
    "amazon.it":"Italy",
    "amazon.es":"Spain",
    "amazon.nl"  :"Netherlands"
}

asin = input("Enter ASIN: ")

# AMAZON DATA
amazon_data = run_program(amazon_dict, asin)
for i in amazon_data:
    print("Title: ", i['title'])
    print("Name: ", i['name'])
    print("Price: ", i['price'])
    print("Link: ", i['link'])
    print("***************")

print("\n")

# FIND TITLE
title_to_search = ""
forbidden = ["Mexico", "Brazil", "Spain", "Italy", "Germany", "Netherlands", "France", "Turkey", "Japan"]
for i in amazon_data:
    title = i['title']
    name = i['name']
    
    if (name not in forbidden):
        if(title != "No Product" and title != "No title information."):
            title_to_search = title

print("TITLE TO SEARCH: ", title_to_search)

if title_to_search != "":
    # EBAY DATA
    ebay_soup = get_data(title_to_search)
    ebay_data = parse(ebay_soup)
    for i in ebay_data:
        print("Title: ", i['title'])
        print("Price: ", i['price'])
        print("Link: ", i['link'])
        print("Image Source: ", i['image_src'])
        print("***************")
    print("\n")
        
    # GOOGLE DATA
    google_data = get_data_google(title_to_search)
    for i in google_data:
        if i['price'] != "No Price":
            print("Title: ", i['title'])
            print("Price: ", i['price'])
            print("Link: ", i['link'])
            print("Store: ", i['store'])
            print("***************")