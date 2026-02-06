import requests
from bs4 import BeautifulSoup
import csv

# Target website (scrape-friendly)
URL = "https://quotes.toscrape.com/"

response = requests.get(URL)

if response.status_code != 200:
    print("Failed to retrieve webpage")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []

quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text")
    author = quote.find("small", class_="author")
    tag_elements = quote.find_all("a", class_="tag")

    quote_text = text.text if text else "N/A"
    author_name = author.text if author else "N/A"
    tags = ", ".join([tag.text for tag in tag_elements])

    quotes_data.append([quote_text, author_name, tags])

# Save to CSV
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])
    writer.writerows(quotes_data)

print("Scraping completed. Data saved to quotes.csv")
