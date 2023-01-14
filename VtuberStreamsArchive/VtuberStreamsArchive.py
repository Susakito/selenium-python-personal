# ARHIVE Vtuber Streams

from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time

PATH = "C:\Program Files\webdriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://archive.is/")

search = driver.find_element_by_name("url")
search.send_keys("https://www.youtube.com/playlist?list=PLE4YuyOC2lYKc6G6A2N50imZu1aIp1Hmm")
search.send_keys(Keys.RETURN)

def find_sign_in(id): #METHOD PARA SA AUTO QUIT # CHECK KUNG NAKITA BA YUNG ELEMENT
    try:
        driver.find_element_by_id(id)
    except:
        return False
    return True

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "save"))
    )

except:
    searchButton = driver.find_element_by_css_selector("#DIVALREADY2 > div > div:nth-child(2) > div > form > div > input[type=submit]")
    searchButton.click()
    while x == False:#LOOP PARA SA AUTOQUIT
        driver.implicitly_wait(10)
        print("in while loop")
        x = find_sign_in("button")
        if x== True:
            driver.quit()

