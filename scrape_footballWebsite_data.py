from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Football"]
mycol = mydb["FootBallData"]

driver.get('https://www.adamchoi.co.uk/overs/detailed')
button = driver.find_element_by_xpath('//label[@class="btn btn-sm btn-primary ng-pristine ng-untouched ng-valid ng-not-empty"]')
button.click()

dropdown = Select(driver.find_element_by_id('country'))  #for drop down mene  to get dataa automatically
dropdown.select_by_visible_text('Spain')



time.sleep(3)

date = []
home_team = []
score = []
away_team = []

matches = driver.find_elements_by_tag_name('tr')
for match in matches:

   date.append(match.find_element_by_xpath('./td[1]').text)
   home_team.append(match.find_element_by_xpath('./td[2]').text)
   score.append(match.find_element_by_xpath('./td[3]').text)
   away_team.append(match.find_element_by_xpath('./td[4]').text)
data=[]
driver.close()
for index, row in enumerate(matches):
    dataa = {
        "date":date[index],
        "Release_Date": home_team[index],
        "score": score[index],
       "Away_team": away_team[index],
    }
    data.append(dataa)

X = mycol.insert_many(data)
