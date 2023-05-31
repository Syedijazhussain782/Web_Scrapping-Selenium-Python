from selenium import webdriver

DRIVER_PATH = 'E:\ijaz_Practice\chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://google.com')