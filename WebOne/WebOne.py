from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)



driver.get('https://store.steampowered.com/')


#driver.get('https://archive.is/')

#searchBox = driver.find_element_by_xpath('//*[@id="url"]')


#searchBox.send_keys('https://www.youtube.com/playlist?list=PLE4YuyOC2lYKi823xbvcOmiblIZWn2sS9')

#seachButton = driver.find_element_by_xpath('//*[@id="submiturl"]/div[3]/input')
#seachButton.click()