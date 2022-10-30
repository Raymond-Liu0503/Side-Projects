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

product = input('Item: ')

PATH = r"C:\Users\raymo\Documents\Coding-Programs\chromedriver.exe"
s=Service(PATH)
driver = webdriver.Chrome(service=s)
driver.get('https://www.amazon.ca/ref=nav_logo')

total_prices = []
temp_list = []
temp_item_names = []
item_names = []
sorted_prices = []

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="twotabsearchtextbox"]'))
    )
finally:
    search = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
    search.send_keys(product)
    search.send_keys(Keys.RETURN)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole"))
        )
    finally:
        temp_prices = driver.find_elements(By.CLASS_NAME, 'a-price-whole')
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.a-size-base-plus.a-color-base.a-text-normal'))
            )
        finally:
            raw_item_names = driver.find_elements(By.CSS_SELECTOR, '.a-size-base-plus.a-color-base.a-text-normal')

            #converts from web element to string values
            for k in range(len(raw_item_names)):
                temp_item_names.append(raw_item_names[k].text)
            
            for i in range(len(temp_prices)):
                num = (temp_prices[i].text)
                edited_num = num.replace(",",'')
                temp_list.append(edited_num)
            
            """ for a in range(len(temp_list)):
                print(f'{temp_item_names[a]} ${temp_list[a]}') """
            #To filter outliers that probably aren't the right product
            for i in range(len(temp_list)):
                try:
                    p = float(temp_list[i])
                    if i > 0:
                        #If the price is within an acceptable range from the most relevant result
                        if p >= total_prices[0]*0.1: 
                            item_names.append(temp_item_names[i])
                            total_prices.append(p)
                    else:
                        item_names.append(temp_item_names[i])
                        total_prices.append(p)
                except:
                    None
            for u in range(len(total_prices)-1):
                sorted_prices.append(total_prices[u])
            sorted_prices.sort()
        
sum = 0

""" for a in range(len(total_prices)):
    print(f'{item_names[a]} ${total_prices[a]}') """

for j in range(len(total_prices)):
    sum = sum + total_prices[j]

average = round(sum/len(total_prices), 2)
print(f'The average price of {product} on amazon.ca is ${average}')

lowest_price = round(sorted_prices[0],2)
highest_price = round(sorted_prices[len(sorted_prices)-1], 2)
print(f'The lowest price of {product} on amazon.ca is ${lowest_price}')
print(f'The highest price of {product} on amazon.ca is ${highest_price}')

driver.quit()