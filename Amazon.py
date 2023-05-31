import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# %matplotlib inline




def get_data(no_pages):
    author=[]
    name=[]
    price=[]
    review=[]

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
               "Accept-Encoding": "gzip, deflate",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1",
               "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    r = requests.get(
        'https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_' + str(no_pages) + '?ie=UTF8&pg=' + str(no_pages),
        headers=headers)  # , proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content, features="lxml")
    # print(soap)
    products = soup.find_all('div', {'class': 'a-column a-span12 a-text-center _cDEzb_grid-column_2hIsc'})
    # print(products)
    for dt in products:

        author.append(dt.find('div', {'class': 'a-row a-size-small'}).text)


        name.append(dt.find('div',{'class':'_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'}).text)



        review.append(dt.find('span',{'class':'a-icon-alt'}).text)


        price.append(dt.find('span',{'class':'_cDEzb_p13n-sc-price_3mJ9Z'}).text)



    for i in products:
        try:

            data={
                "BookName":name,
                "AuthorName":author,
                "Rating":review,
                "price":price
            }

        except:
            pass


    return data




no_pages =1
data=get_data(no_pages)
print(data)