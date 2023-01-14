# ARHIVE VTUBER HELL CLIPS AND STREAMS


from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait

PATH = "C:\Program Files\webdriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://archive.is/")

search = driver.find_element_by_name("url")
search.send_keys("https://www.youtube.com/playlist?list=PLE4YuyOC2lYKCQVgaoYcE4lDoFd_uLcVl")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "save"))
    )

except:
    searchButton = driver.find_element_by_css_selector("#DIVALREADY2 > div > div:nth-child(2) > div > form > div > input[type=submit]")
    searchButton.click()
    time.sleep(3600)
    driver.quit()


driver.quit()




#driver.implicitly_wait(10)











#print(driver.page_source)

#driver.quit()
#https://archive.is/