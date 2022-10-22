from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

#gets input from the user
player = input('Enter a player: ')

from selenium.webdriver.chrome.options import Options

#headless
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.nfl.com/players/')

#searches the player in the nfl database
search = driver.find_element(By.ID, "player-search-input")
search.send_keys(player)
search.send_keys(Keys.RETURN)

#clicks on the player profile link
p_link_search = driver.find_element(By.XPATH, "//div[@class='d3-o-media-object']//a[@class='d3-o-player-fullname nfl-o-cta--link']")
p_link_search.click()

#collects data
attributes = driver.find_elements(By.CLASS_NAME, "nfl-c-player-info__value")
name = driver.find_element(By.CLASS_NAME, "nfl-c-player-header__title").text
position = driver.find_element(By.CLASS_NAME, "nfl-c-player-header__position").text

#organizes measurements
measurements = []
for i in range(len(attributes)):
    measurements.append(attributes[i].text)

#outputs collected data
os.system('cls')
print(f'Player: {name}')
print(f'Position: {position}')
print(f'Height: {measurements[0]}')
print(f'Weight: {measurements[1]} lbs')
print(f'Arm length (inches): {measurements[2]}')
print(f'Hand size (inches): {measurements[3]}')
print(f'Experience: {measurements[4]} years')
print(f'College: {measurements[5]}')
print(f'Age: {measurements[6]}')

driver.quit()


