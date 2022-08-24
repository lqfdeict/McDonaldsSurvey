#Automating Test clone 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By


PATH = "D:\chromedriver.exe "

driver = webdriver.Chrome(PATH)

driver.get('https://www.youtube.com/');



search_box = driver.find_element("name", "search_query")

search_box.send_keys('ChromeDriver')

search_box.submit()


# MAKE EACH LINE HAVE ITS OWN THING
# initialize(1334)
# def initialize(n):
#     search_box = driver.find_element("name", "CN1")
#     search_box.send_keys(n)

