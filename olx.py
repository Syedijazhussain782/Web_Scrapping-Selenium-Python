import requests
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait


driver=webdriver.Chrome()
resp=driver.get("https://www.olx.com.pk/items/q-mobile-phones?")
# Wait for the page to load


total = 10                                                  #page Loaoding TO END
countt = 1
while countt < total:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.find_element_by_class_name('_31a14546').click()
    time.sleep(1)
    countt=countt+1




# time.sleep(3)
# # Scroll down the page by pressing the END key
# body = driver.find_element_by_tag_name('body')
# body.send_keys(Keys.END)
# # Wait for the page to load more content
# #time.sleep(3)
# # Scroll down again
# body.send_keys(Keys.END)


articles=driver.find_elements_by_xpath('//article[@class="_7e3920c1"]')
name=[]
price=[]
location=[]
image=[]
for article in articles:
    name.append(article.find_element_by_class_name("a5112ca8").text)
    price.append(article.find_element_by_class_name("_95eae7db").text)
    location.append(article.find_element_by_class_name("_424bf2a8").text)
    find_href = article.find_element_by_class_name('_943b7102')
    time.sleep(2)
    image.append(find_href.get_attribute("src"))

print(name)
print(price)
print(location)
print(image)



