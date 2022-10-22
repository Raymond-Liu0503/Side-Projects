from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

#gets input from user
location = input('Enter a city: ')

from selenium.webdriver.chrome.options import Options

#headless
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com/')

#locates the search bar
search = driver.find_element(By.NAME, "q")

#inputs the user input into the search bar to find the weather forecast
search.send_keys('weather today in '+location)
search.send_keys(Keys.RETURN)

#current weather
cur_temp = driver.find_element(By.ID, 'wob_tm').text #finds the current temperature
cur_cond = driver.find_element(By.ID, 'wob_dc').text #finds the current weather condition

#Forecast
d_list = driver.find_elements(By.CLASS_NAME, 'Z1VzSb')
c_list = driver.find_elements(By.XPATH, "//div[@class='DxhUm']//img[@class='uW5pk']")
ht_list = driver.find_elements(By.XPATH, "//div[@class='gNCp2e']//span[@style='display:inline']")
lt_list = driver.find_elements(By.XPATH, "//div[@class='QrNVmd ZXCv8e']//span[@style='display:inline']")
days = []
cond = []
h_temp = []
l_temp = []

#output current weather
print(f'It is currently {cur_temp} degrees celsius and {cur_cond} in {location}')

#collects data and organizes them into lists
#prints forecast
for i in range(0,7):
    days.append(d_list[i].text)
    cond.append(c_list[i].get_attribute('alt'))
    h_temp.append(ht_list[i].text)
    l_temp.append(lt_list[i].text)
    print(f'On {days[i]} it will be {cond[i]} with a high of {h_temp[i]} and a low of {l_temp[i]} degrees')

option = 0

driver.quit()