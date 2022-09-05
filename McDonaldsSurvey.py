
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by   import By

PATH = "C:\chromedriver.exe "

driver = webdriver.Chrome(PATH)

driver.get('https://www.mcdvoice.com/');


#code = "12345678912345678912345678"
code = input("Enter the 26 digit code: ")


CN1 = code[0] + code[1] + code[2] + code[3] + code[4]
CN2 = code[5] + code[6] + code[7] + code[8] + code[9]
CN3 = code[10] + code[11] + code[12] + code[13] + code[14]
CN4 = code[15] + code[16] + code[17] + code[18] + code[19]
CN5 = code[20] + code[21] + code[22] + code[23] + code[24]
CN6 = code[25]


search = driver.find_element("name", "CN1")

search.send_keys(CN1)

search = driver.find_element("name", "CN2")

search.send_keys(CN2)

search = driver.find_element("name", "CN3")

search.send_keys(CN3)

search = driver.find_element("name", "CN4")

search.send_keys(CN4)

search = driver.find_element("name", "CN5")

search.send_keys(CN5)

search = driver.find_element("name", "CN6")

search.send_keys(CN6)


search.submit()

#How did you place your order?
link = driver.find_element("id", "textR000455.1")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

#Please select your visit type
link = driver.find_element("id", "textR004000.2")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

#please rate your overall satisfaction with your experience at this McDonalds
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[1]/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

#Are you a member of MyMcDonalds Rewards
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[2]/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

#Did the employee ask if you were using your mobile app?
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[2]/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()


#six page one
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[1]/td[1]/label")
link.click()


#2nd
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[2]/td[1]/label")
link.click()


#3rd
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[3]/td[1]/label")
link.click()


#4th
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[4]/td[1]/label")
link.click()


#5th
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[5]/td[1]/label")
link.click()


#6th
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[6]/td[1]/label")
link.click()


link = driver.find_element("id", "NextButton")
link.click()

link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[1]/td[1]/label")
link.click()
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[2]/td[1]/label")
link.click()

link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[3]/td[1]/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()


#What items did you order?
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/fieldset/div/div/div[1]/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[1]/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[2]/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[1]/td[1]/label")
link.click()
link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr[2]/td[1]/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

review = "Overall the customer service was superb. How each employee help out was great. The order was taken quickly and completed very quickly. Great experience."

search = driver.find_element("name", "S081000")

search.send_keys(review)
link = driver.find_element("id", "NextButton")
link.click()

link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[2]/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/fieldset/div/div/div[1]/span/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/fieldset/div/div/div[2]/span/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

link = driver.find_element("xpath", "/html/body/div[1]/main/div[2]/form/div/table/tbody/tr/td[1]/label")
link.click()
link = driver.find_element("id", "NextButton")
link.click()

finalcode = driver.find_element("class","ValCode")
print(finalcode)


