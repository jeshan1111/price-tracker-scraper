# Price Tracker Scraper

A Python-based web scraper designed to extract product data from an e-commerce website and save it to a CSV file. This tool is ideal for businesses or individuals needing to monitor product prices, track competitor data, or collect structured product information for market analysis.

## 🚀 Features
- Scrapes Product Data: Extracts product names, prices, and descriptions from the test e-commerce site webscraper.io.
- CSV Output: Saves data in a clean, structured CSV file, ready for use in Excel or other tools.
- Error Handling: Robustly handles missing data to ensure reliable scraping.
- Portfolio Showcase: Demonstrates skills in Python, web scraping, and data processing for freelance opportunities.

## 📋 What It Does
This script automates the process of collecting product information from an e-commerce website. It:

1. Sends an HTTP request to fetch the webpage.
2. Parses the HTML to extract product names, prices, and descriptions.
3. Organizes the data into a structured format.
4. Saves the results to products.csv for easy client delivery.

This is a practical tool for freelance gigs like price monitoring, competitor analysis, or data collection for market research.

## 🛠️ How to Run It
Follow these steps to run the scraper on your own machine:

1. Ensure Python 3 is installed (check with: python3 --version)
2. Set up a virtual environment (recommended):
   python3 -m venv myenv
   source myenv/bin/activate
3. Install required packages:
   pip install requests beautifulsoup4 pandas
4. Run the script:
   python price_tracker.py
5. Check the output:
   - A products.csv file will be created in your directory.
   - A preview of the scraped data will be printed in the terminal.

## ✅ Example Output
The script generates a products.csv file with columns:

- Product Name: The name of the product.
- Price: The price listed on the website.
- Description: A brief product description.

Sample products.csv (included in the repository):

Product Name,Price,Description
"Dell Latitude E7270","$1099.00","Dell Latitude E7270, 12.5 inch..."
"Asus ROG Strix GL553VD","$1299.00","Asus ROG Strix GL553VD, 15.6 inch..."

## 🧭 What I Learned
- Web Scraping: Using requests to fetch web pages and BeautifulSoup to parse HTML and extract specific elements.
- Data Processing: Leveraging pandas to organize scraped data into a structured CSV format.
- Error Handling: Implementing checks to handle missing or malformed data gracefully.
- Freelance Applications: Building tools that meet real-world needs, such as price monitoring for e-commerce businesses.
