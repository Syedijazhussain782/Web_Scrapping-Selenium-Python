import requests
from bs4 import BeautifulSoup
import pandas

url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=camera&_sacat=0&rt=nc&LH_PrefLoc=6"
r = requests.get(url)
soup = BeautifulSoup(r.text ,"html.parser")
#print(soup.text)

products=soup.find_all('div', {'class': 's-item__wrapper clearfix'})
print(products)
for product in products:
    all_product = []

    title = product.find('div', {'class': 's-item__title'}).text
    price= (product.find('span', {'class': 's-item__price'}).text.replace('$', ''))
    try:
        Made_in= product.find('span', {'class': 's-item__location s-item__itemLocation'}).text
    except:
        Made_in = ""
    link = product.find('a', {'class': 's-item__link'})['href']

    pp = {
        "title": title,
        "price" : price,
        "Made_In" : Made_in,
        "link": link
    }
    all_product.append(pp)
    df = pandas.DataFrame(all_product)
    csvfile = df.to_csv('ab.csv', index=False)



    # import pdb;pdb.set_trace()
    # result={
    #     'title': product.find('div', {'class': 's-item__title'}).text,
    #     'price':(product.find('span', {'class': 's-item__price'}).text.replace('$', '')),
    #     'Made in':product.find('span', {'class': 's-item__location s-item__itemLocation'}).text,
    #     'link': product.find('a',{'class': 's-item__link'})['href'],

    # }




