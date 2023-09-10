import requests
import unicodedata
from bs4 import BeautifulSoup
import pandas as pd
import json


def decode_unicode_escape(price_str):
    return unicodedata.normalize('NFKD', price_str).encode('ascii', 'ignore').decode('utf-8')

def scrape_flipkart(search_keyword, num_pages=5):
    base_url = "https://www.flipkart.com"
    products = []
    
    for page in range(1, num_pages + 1):
        url = f"{base_url}/search?q={search_keyword}&page={page}"
        response = requests.get(url)
        print(url)
        if response.status_code != 200:
            print(f"Failed to retrieve page {page}. Status code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        product_cards = soup.find_all("div", class_="_2kHMtA")
        
        for card in product_cards:
                title = card.find("a", class_="_1fQZEK").text
                price_str = card.find("div", class_="_30jeq3").text
                price = decode_unicode_escape(price_str)
                product_link = base_url + card.find("a", class_="_1fQZEK")["href"]
                products.append({
                    "Title": title,
                    "Price": price,
                    "Link": product_link
                })
    return products

if __name__ == "__main__":
    search_keyword = "laptop"  # Change this to your desired search keyword
    num_pages_to_scrape = 5  # Number of pages to scrape (each page typically has 24 products)
    
    scraped_data = scrape_flipkart(search_keyword, num_pages_to_scrape)
    
    if scraped_data:
        # df = pd.DataFrame(scraped_data)
        json_data = json.dumps(scraped_data, indent=4)
        with open('scraped_data.json', 'w') as json_file:
            json_file.write(json_data)
            print("Data has been scraped and stored in 'scraped_data.json'.")
        # df.to_json(f"{search_keyword}_products.json", orient="records", lines=True, indent=4)
        print("Scraping completed. Data saved to CSV.")
    else:
        print("No data was scraped.")


