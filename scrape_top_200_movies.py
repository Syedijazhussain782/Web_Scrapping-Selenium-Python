from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["TOP200MOVIES"]
mycol = mydb["MoviesDetail"]


driver = webdriver.Chrome()
driver.get('https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW')
movies_names = driver.find_elements_by_xpath('//td[@class="a-text-left mojo-field-type-title"]/a[@class="a-link-normal"]')
movie_name_list = []
for movie in range(len(movies_names)):
    movie_name_list.append(movies_names[movie].text)
# print(movie_name_list)

release_year = driver.find_elements_by_xpath('//td[@class="a-text-left mojo-field-type-year"]/a[@class="a-link-normal"]')
release_year_list = []
for year in range(len(release_year)):
    release_year_list.append(release_year[year].text)
# print(release_year_list)

life_time_gross = driver.find_elements_by_xpath('//td[@class="a-text-right mojo-field-type-money"]')
life_time_gross_list = []
for gross in range(len(life_time_gross)):
    life_time_gross_list.append(life_time_gross[gross].text)
# print(life_time_gross_list)
driver.close()
data = []
for index, row in enumerate( movie_name_list):
    dataa = {
        "Movies_name":movie_name_list[index],
        "Release_Date": release_year_list[index],
        "Lifetime_Earnings": life_time_gross_list[index],
    }
    data.append(dataa)
# data = list(zip(movie_name_list, release_year_list, life_time_gross_list))
# convert multiple lists into 1 tuple and then convert to 1 list
# # print(data)
#
# df = pd.DataFrame(data, columns=['Movies_name', 'Release_Date', 'Lifetime_Earnings'])
#
# dataa=df.to_json(orient='records')
print(data)
import pdb;pdb.set_trace()
X = mycol.insert_many(data)
