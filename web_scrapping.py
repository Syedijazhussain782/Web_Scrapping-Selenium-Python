import requests
from  bs4 import BeautifulSoup
from urllib.request import urlopen
import json


r=requests.get("http://olympus.realpython.org/profiles/aphrodite")
#print(r.status_code)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


text=soup.get_text()

print(text)
image=soup.find_all("img")


print(image)

testjson={                                            # sunny Bahi      Convert data  from text formate to json formate
"Profile": "Aphrodite",
"Name": "Aphrodite",
"Favorite animal": "Dove",
"Favorite color": "Red",
"Hometown": "Mount Olympus"

}

with open('data.json', 'w') as f:
    json.dump(testjson, f)

