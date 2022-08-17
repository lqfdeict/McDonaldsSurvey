# tutorial for selenium : "https://www.youtube.com/watch?v=b5jt2bhSeXs&ab_channel=TechWithTim"

from selenium import webdriver

PATH = "C:\chromedriver.exe "

driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")




driver.close()


