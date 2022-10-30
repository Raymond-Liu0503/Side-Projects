import discord
from discord.ext import commands

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

client = commands.Bot(command_prefix='$')
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

t1_players = []
t2_players = []

#Gets data from espn fantasy football stats website
def find_players(p_name, player_num):
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
                        print('the avg is: ',avg)
                        return avg
                        #driver.quit()

#calculations
def run_trade(team):
    t1_avg = 0
    t2_avg = 0

    #logic for determining the value of each side of the trade
    if team == 1:
        for i in range(len(t1_players)):
            t1_avg = t1_avg + find_players(t1_players[i], i)
        return t1_avg
    else:
        for j in range(len(t2_players)):
            t2_avg = t2_avg + find_players(t2_players[j], j)
        return t2_avg

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def trade(ctx):
    #gets input from user
    await ctx.send('Welcome to the ESPN Fantasy Football Trade Analyzer')

    await ctx.send(f"Enter the players team 1 is sending (format: player1, player 2): ")
    msg = await client.wait_for("message")
    temp1 = msg.content.lower()
    team1_input = temp1.split(', ')
    for i in range(len(team1_input)):
        t1_players.append(team1_input[i])
    
    await ctx.send(f"Enter the players team 2 is sending (format: player1, player 2): ")
    msg = await client.wait_for("message")
    temp2 = msg.content.lower()
    team2_input = temp2.split(', ')
    for j in range(len(team2_input)):
        t2_players.append(team2_input[j])
    
    #calculates the value of each side
    await ctx.send('Calculating...')

    t1_avg = run_trade(1)
    t2_avg = run_trade(2)
    t1_value = t2_avg/len(t2_players)
    t2_value = t1_avg/len(t1_players)
    
    #determines the winner
    trade_winner = None

    if t1_value > t2_value:
        trade_winner = 'Team 1'
    elif t2_value > t1_value:
        trade_winner = 'Team 2'
    else:
        await ctx.send('The trade is equally fair for both sides')
    
    #output
    embed=discord.Embed(title=f"{ctx.author}'s trade")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.add_field(name="Team 1:", value=t1_players, inline=True)
    embed.add_field(name="Team 2:", value=t2_players, inline=True)
    embed.add_field(name="Team 1 value:", value=t1_value, inline=True)
    embed.add_field(name="Team 2 value:", value=t2_value, inline=True)
    embed.add_field(name="Winner of the trade:", value=trade_winner, inline=False)
    await ctx.send(embed=embed)
    driver.quit()


client.run('token')
