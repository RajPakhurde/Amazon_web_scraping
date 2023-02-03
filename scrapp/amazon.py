import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Make a request to the Amazon website and parse the HTML using BeautifulSoup
url = "https://www.amazon.com/s?field-keywords=laptops"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract the product information from the HTML
products = []
for product in soup.find_all("div", class_="s-result-item"):
    name = product.find("h2").text
    price = float(product.find("span", class_="a-offscreen").text[1:].replace(",", ""))
    products.append({"name": name, "price": price})

# Create a DataFrame from the product information
df = pd.DataFrame(products)

# Remove missing values from the DataFrame
cleaned_df = df.dropna()

# Plot the average price of products
plt.plot(cleaned_df.groupby("price").mean()["price"])

# Add labels and title to the plot
plt.xlabel("Price")
plt.ylabel("Average Price")
plt.title("Average Price of Products")

# Show the plot
plt.show()
