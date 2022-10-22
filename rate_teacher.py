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

#headless
#chrome_options = Options()
#chrome_options.add_argument("--headless")
#driver = webdriver.Chrome(options=chrome_options)

#gets input from the user
teacher = input('Enter a teacher:')

#pre-headless code
PATH = r"C:\Users\raymo\Documents\Coding-Programs\chromedriver.exe"
s=Service(PATH)
driver = webdriver.Chrome(service=s)
#driver = webdriver.Chrome(PATH)

driver.get('https://www.ratemyprofessors.com/')

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div/button'))
    )
finally:
    close = driver.find_element(By.XPATH,'/html/body/div[5]/div/div/button')
    close.click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[3]/div[1]/div[3]/div[2]/input'))
        )
    finally:
        search = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[3]/div[1]/div[3]/div[2]/input')
        search.send_keys('Carleton University')
        time.sleep(0.30)
        search.send_keys(Keys.RETURN)

        search.send_keys(teacher)
        search.send_keys(Keys.RETURN)

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[3]/a/div'))
            )
        finally:
            prof = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[3]/a/div')
            prof.click()

            try:
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[1]/div[1]/div/div[1]'))
                )
            finally:
                rating = float(driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[1]/div[1]/div/div[1]').text)
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[1]/div[2]/div[1]'))
                )
                finally:
                    prof_info = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[1]/div[2]/div[1]').text
                    os.system('cls')
                    print(prof_info)
                    print(f'Rating: {rating}/5')
                    if rating <= 3:
                        print('The prof is dogshit')

    driver.quit()