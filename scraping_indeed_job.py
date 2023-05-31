from selenium import webdriver
import pandas as pd
import time


#Database Connectivity
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["indeedJob"]
mycol = mydb["indeed"]




driver = webdriver.Chrome()
driver.get("https://www.indeed.com/q-data-scientist-jobs.html")
time.sleep(2)

job_details=[]
job_title=[]
job_company=[]
job_location=[]
job_summary=[]
job_publish_date =[]



job_list = driver.find_elements_by_xpath('//div[@class="jobTitle-d3aa0dd9a8f51072"]')
print(job_list)
for each_job in job_list:
    # Getting job info
    job_title.append(each_job.find_elements_by_xpath('.//h2[@class="title"]/a').text)
    job_company.append(each_job.find_elements_by_xpath('.//span[@class="company"]').text)
    job_location.append(each_job.find_elements_by_xpath('.//span[@class="location accessible-contrast-color-location"]').text)
    job_summary.append(each_job.find_elements_by_xpath('.//div[@class="summary"]').text)
    job_publish_date.append(each_job.find_elements_by_xpath('.//span[@class="date"]').text)
    # Saving job info

#driver.quit()
print(job_title)
print(job_company)
print(job_location)
print(job_summary)
print(job_publish_date)




#data=[]
#for index, row in enumerate(job_title):
 #   dataa = {
  #     "job_company ": job_company [index],
   #     "job_location":job_location[index],
    #   "job_summary":job_summary [index],
     #   "job_publish_date":job_publish_date[index],

 #   }
  #  data.append(dataa)

#X = mycol.insert_many(data)


