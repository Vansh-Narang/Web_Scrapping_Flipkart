import requests
from bs4 import BeautifulSoup
import urllib.request as ur
import pandas as pd
# Getting input for webiste from user
url_input = input("Enter url :")
print(" This is the website link that you entered", url_input)


# For extracting specific tags from webpage
def getTags(tag):
    s = ur.urlopen(url_input)
    soup = BeautifulSoup(s.read())
    return soup.findAll(tag)

# For extracting all h1-h6 heading tags from webpage
def headingTags(headingtags):
    h = ur.urlopen(url_input)
    soup = BeautifulSoup(h.read(),'html.parser')
    print("List of headings from headingtags function h1, h2, h3, h4, h5, h6 :")
    for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        print(heading.name + ' ' + heading.text.strip())


def price_tag():
    data_source =ur.urlopen(url_input)
    soup =BeautifulSoup(data_source.read(),'html.parser')
    prices=soup.find_all(class_="price")
    print("Price of products :")
    for price in prices:
        price_text=price.get_text()
        print(price_text)

# For extracting specific title & meta description from webpage


def titleandmetaTags():
    s = ur.urlopen(url_input)
    soup = BeautifulSoup(s.read(),'html.parser')
    # ----- Extracting Title from website ------#
    title = soup.title.string
    print('Website Title is :', title)
    # -----  Extracting Meta description from website ------#
    meta_description = soup.find_all('meta')
    for tag in meta_description:
        if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
            # print ('NAME    :',tag.attrs['name'].lower())
            print('CONTENT :', tag.attrs['content'])

if __name__ == '__main__':
    # titleandmetaTags()
    # price_tag()
    tags = getTags('a')
    headtags = headingTags('h1')
    for tag in tags:
        print(tag, tag.contents)

df = pd.DataFrame(price_tag())
df.to_json("_products.json", orient="records", lines=True, indent=4)
print("Scraping completed. Data saved to CSV.")