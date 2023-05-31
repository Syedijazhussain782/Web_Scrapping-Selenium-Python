import requests
import time
from bs4 import BeautifulSoup
import json
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()

target_url = "https://www.nasdaq.com/market-activity/stocks/tsla"
driver.get(target_url)
import pdb;pdb.set_trace()
html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.END)
time.sleep(2)
resp = driver.page_source


soup = BeautifulSoup(resp, 'html.parser')

obj = {}
l=list()


try:
    obj["name"]=soup.find("span",{"class":"symbol-page-header__name"}).text
except:
    obj["name"]=None
try:
    obj["askPrice"]=soup.find("span",{"class":"symbol-page-header__pricing-ask"}).text
except:
    obj["askPrice"]=None
tables = soup.find("table",{"class":"summary-data__table"}).find_all("tbody",{"class":"summary-data__table-body"})
print(tables)
try:
    table1 = tables[0]

    table2=tables[1]
except:
    pass
try:
    obj["P/E Ratio"]=table2.find_all("tr",{"class":"summary-data__row"})[0].find("td",{"class":"summary-data__cell"}).text
except:
    obj["P/E Ratio"]=None
try:
    obj["1-year budget"]=table1.find_all("tr",{"class":"summary-data__row"})[3].find("td",{"class":"summary-data__cell"}).text
except:
    obj["1-year budget"]=None
try:
    obj["Dividend"]=table2.find_all("tr",{"class":"summary-data__row"})[7].find("td",{"class":"summary-data__cell"}).text
except:
    obj["Dividend"]=None
l.append(obj)
obj={}
print(l)

driver.close()
#[{'name': 'Tesla, Inc. Common Stock (TSLA)', 'askPrice': '$162.55', 'P/E Ratio': None, '1-year budget': None, 'Dividend': None}]