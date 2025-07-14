import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the test e-commerce site
url = "https://webscraper.io/test-sites/e-commerce/allinone"

# Send GET request to fetch the page
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to fetch page: {response.status_code}")
    exit()

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all product cards (they use the 'thumbnail' class)
products = soup.find_all("div", class_="thumbnail")

# Lists to store product data
names = []
prices = []
descriptions = []

# Extract data from each product
for i, product in enumerate(products, 1):
    # Get product name
    name_tag = product.find("h4", class_="title")
    name = name_tag.text.strip() if name_tag else "Missing Name"
    # Get price
    price_tag = product.find("h4", class_="price")
    price = price_tag.text.strip() if price_tag else "Missing Price"
    # Get description
    desc_tag = product.find("p", class_="description")
    desc = desc_tag.text.strip() if desc_tag else "Missing Description"

    print(f"Product {i}: Name={name}, Price={price}, Description={desc}")

    names.append(name)
    prices.append(price)
    descriptions.append(desc)

# Create a DataFrame with the data
data = {
    "Product Name": names,
    "Price": prices,
    "Description": descriptions
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("products.csv", index=False)
print("Data saved to products.csv")

# Print a preview of the data
print("\nScraped Products:")
print(df)
