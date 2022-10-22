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

destination = input('Destination: ')

PATH = r"C:\Users\raymo\Documents\Coding-Programs\chromedriver.exe"
s=Service(PATH)
driver = webdriver.Chrome(service=s)
driver.get('https://maps.google.com/')

search = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
search.send_keys(destination)
search.send_keys(Keys.RETURN)

#There are two possiblities for google maps search, either you search a specific location with one address or you search for something that has multiple locations (like McDonalds)
#This is why you need to test for the first possiblity (one specific location) before moving onto the outcome with multiple locations
try:
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/img'))
        )
    finally:
        direction_but = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button/span/img').click()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="sbsg51"]'))
            )
        finally:
            location = driver.find_element(By.XPATH, '//*[@id="sbsg51"]').click()
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button/img'))
                )
            finally:
                car = driver.find_element(By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button/img').click()
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH,'//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]'))
                    )
                finally:
                    e_time = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]').text
                    route = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-title-0"]/span').text
                    print(f'It will take approx. {e_time} via {route}')
except:
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div[2]/button/span'))
        )
    finally:
        alt_dir = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div[2]/button/span').click()
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="sbsg51"]'))
            )
        finally:
            location = driver.find_element(By.XPATH, '//*[@id="sbsg51"]').click()
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button/img'))
                )
            finally:
                car = driver.find_element(By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]/button/img').click()
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH,'//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]'))
                    )
                finally:
                    e_time = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]').text
                    route = driver.find_element(By.XPATH, '//*[@id="section-directions-trip-title-0"]/span').text
                    print(f'It will take approx. {e_time} via {route}')
time.sleep(1)
driver.quit()