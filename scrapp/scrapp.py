import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.com/products"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, "html.parse")

    product_listing = soup.find_all("div",class_="product-listing")

    prodcuts = []

    for listing in product_listing:

        product_name = listing.find("h3").text
        product_price = listing.find("span", class_="product-price").text
        product_reviews = listing.find("span", class_="product-reviews").text

        prodcuts.append({
            "name": product_name,
            "price": product_price,
            "reviews": product_reviews
         })

    
    df = pd.DataFrame(prodcuts)

    print(df)

else:
    print("Failed to be retrived website")



