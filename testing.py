#Automating Test clone 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

PATH = "D:\chromedriver.exe "

driver = webdriver.Chrome(PATH)

driver.get('https://www.youtube.com/');

def initialform():

    search = driver.find_element("name", "search_query")

    search.send_keys('ChromeDriver')

    search.submit()


# MAKE EACH LINE HAVE ITS OWN THING
# initialize(1334)
# def initialize(n):
#     search = driver.find_element("name", "CN1")
#     search.send_keys(n)

initialform()
