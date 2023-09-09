import pandas as pd
import requests
import json
from bs4 import BeautifulSoup


products=[]
prices_list=[]
desc=[]
reviews=[]




for i in range(2,10):
    url="https://www.flipkart.com/search?q=mobiles%20under%2050000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    r=requests.get(url) 
    #status code
print(r.status_code)

    #mulitple products

soup=BeautifulSoup(r.text,"lxml")
    #extracting text
    # print(soup)

names=soup.find_all("div",class_="_4rR01T")
# print(names)


for i in names:
    name=i.text
    products.append(name)
# print(products)    

prices=soup.find_all("div",class_="_30jeq3 _1_WHN1")

for i in prices:
    price=i.text
    prices_list.append(price)

# print(prices_list) 


df=pd.DataFrame({"Product Name":products,"Prices":prices_list})
print(df)
df.to_json("data1.json")
# df.to_csv("data2.csv")