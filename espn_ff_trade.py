from argparse import Action
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.chrome.service import Service

# PATH = r"C:\Users\raymo\Documents\Coding-Programs\chromedriver.exe"
# s=Service(PATH)
# driver = webdriver.Chrome(service=s)

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

t1_avg = 0
t2_avg = 0

t1_players = ['mike evans','drake london']
t2_players = ['deebo samuel']

#num_players1 = int(input('# of players team 1 recieving: '))
#num_players2 = int(input('# of players team 2 recieving: '))

#grabs data from the espn fantasy website
def find_players(p_name, player_num):
    global t1_players
    driver.get('https://fantasy.espn.com/football/leaders?statSplit=currSeason&scoringPeriodId=0')

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div/div/input'))
        )
    finally:
        search = driver.find_element(By.XPATH, '//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div/div/input')
        search.send_keys(p_name)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]'))
            )
        finally:
            player_info = driver.find_element(By.XPATH, '//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[2]/div[1]/div/div[2]/div[1]/div[2]').click()
            try:
                element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div/div/div/table[1]/tbody/tr/td[1]/div/div/div[2]/div/div[1]/span[1]/a'))
            )
            finally:
                profile = driver.find_element(By.XPATH, '//*[@id="fitt-analytics"]/div/div[5]/div[2]/div[3]/div/div/div/div/div/div/table[1]/tbody/tr/td[1]/div/div/div[2]/div/div[1]/span[1]/a').click()
                try:
                    element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="fitt-analytics"]/div/div[8]/div/div[2]/div/div[2]/div[2]/section/header/div/div/div[3]/div[3]/div[2]/div[2]'))
                )
                finally:
                    temp_avg = driver.find_element(By.XPATH, '//*[@id="fitt-analytics"]/div/div[8]/div/div[2]/div/div[2]/div[2]/section/header/div/div/div[3]/div[3]/div[2]/div[2]').text
                    avg = float(temp_avg)
                    return avg
                    #driver.quit()

#logic for determining the value of each side of the trade
for i in range(len(t1_players)):
    t1_avg = t1_avg + find_players(t1_players[i], i)

for j in range(len(t2_players)):
    t2_avg = t2_avg + find_players(t2_players[j], j)

t2_value = t1_avg/len(t1_players)
t1_value = t2_avg/len(t2_players)

#outputs the results
os.system('cls')

print('Team 1 sends: ')
for k in range(len(t1_players)):
    print(t1_players[k])

print('')

print('Team 2 sends: ')
for v in range(len(t2_players)):
    print(t2_players[v])

print(f'Team 1 value: {t1_value}')
print(f'Team 2 value: {t2_value}')
if t1_value > t2_value:
    print('Team 1 wins the trade')
elif t2_value > t1_value:
    print('Team 2 wins the trade')
else:
    print('The trade is equally fair for both sides')

driver.quit()
    




