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

tar_stock = input('Enter the stock you want to look up: ')

PATH = r"C:\Users\raymo\Documents\Coding-Programs\chromedriver.exe"
s=Service(PATH)
driver = webdriver.Chrome(service=s)
driver.get('https://ca.finance.yahoo.com/')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="yfin-usr-qry"]'))
    )
finally:
    search = driver.find_element(By.XPATH, '//*[@id="yfin-usr-qry"]')
    search.send_keys(tar_stock)
    search.send_keys(Keys.RETURN)

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')) and EC.presence_of_element_located((By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[3]/span'))
        )
    finally:
        s_value = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]').text
        change = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[3]/span').text
        print(f'Current value: {s_value} ({change})')

driver.quit()