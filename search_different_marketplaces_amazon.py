# IMPORT RELATED LIBRARIES
from bs4 import BeautifulSoup
import requests
import concurrent.futures

# SET INITIAL VARIABLES
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
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

# WILL RETURN title, name, price and url of the product
def get_price(url, asin, name):
    URL = 'https://www.{}/dp/{}'.format(url, asin)
    
    page = requests.get(URL, headers=headers)
    if (page.status_code == 404):
        return "No Product", name, "No Product", URL, "No Image Source information."
    soup1 = BeautifulSoup(page.content, "lxml")
    soup2 = BeautifulSoup(soup1.prettify(), "lxml")
    
    # GET TITLE
    try:
        title = soup2.find('span', {'id': 'productTitle'}).get_text()
    except:
        title = "No title information."
    
    # GET IMAGE_SRC
    try:
        image_src = soup2.find(id='imgTagWrapperId').find('img')['src']
    except:
        image_src = "No Image Source information."
    
    price_label = soup2.find(id="apex_desktop") # Get main price div by id.
    # GET PRICE
    try:
        price = price_label.find_all("span", class_ = "a-offscreen")
    except:
        try:
            price = list(soup2.find(id="price"))
        except:
            price = []
    # SET PRICE TEXT
    price_text = ""
    a = 0
    for i in price:
        price_text += i.get_text().strip() + " - "
        a += 1
        if (a == 2):
            break
    title = title.strip()
    if " - " in price_text:
        price_text = price_text[:-3]
    
    return title, name, price_text, URL, image_src

def execute_get_price(url, asin, name):
    title, name, price, URL, image_src = get_price(url, asin, name)
    if (title == "No title information." or price==""):
        count = 3
        while count > 0:
            title, name, price, URL, image_src = get_price(url, asin, name)
            if (title != "No title information."):
                break
            count -= 1
    return title, name, price, URL, image_src

def run_program(amazon_dict, asin):
    # To use threading, we use concurrent.futures.ThreadPoolExecutor()
    return_list = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = []
        # Looping through different amazon stores.
        for url,name in amazon_dict.items():
            results.append(executor.submit(execute_get_price, url, asin, name))
        #results = [executor.submit(get_price, url, asin, name) for url,name in amazon_dict.items()]
        for f in concurrent.futures.as_completed(results):
           title, name, price, URL, image_src = f.result()
           product = {
                "title": title,
                'name': name,
                'price': price,
                'link': URL,
                'image_src': image_src
           }
           return_list.append(product)
    return return_list

"""
threads = []

asin = "B0009U5OSO"
for url, name in amazon_dict.items():
    thread = threading.Thread(target=get_price, args=(url, asin, name, ))
    threads.append(thread)
    
    #price = get_price(url, asin)
    #print(name, "-", price)
    
for i in threads:
    i.start()
"""  
