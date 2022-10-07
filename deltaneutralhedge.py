from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
from io import open as iopen
from time import sleep
from datetime import datetime as d
import requests
import os
import json
from re import sub
from decimal import Decimal
import requests
import json
from random import randint
import math
zapWebhook = 'https://hooks.zapier.com/hooks/catch/12937216/bgmce86/?'
textzapWebhook = 'https://hooks.zapier.com/hooks/catch/12937216/bg8ekac/?'

jsonHeaders = {'Content-Type': 'application/json'}
# directory = 'C:\\Users\\igor\\PycharmProjects\\scrape-perpetualpools\\'
#position = int(input("Short 3x_BTC_SMA[1] or Long 3x_BTC_SMA[2])"))
#if position == 1:
'''

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
result = json.dumps(crypto_tvlv2, cls=DecimalEncoder)

'''
def tracer_webscrape():
    PATH = '/Users/danielchen/Desktop/chromedriver'
    browser = webdriver.Chrome(PATH)
    sttime = d.now().strftime('%Y%m%d_%H:%M:%S ,')
    urlv2 = "https://pools.tracer.finance/trade/"
    browser.get(urlv2)
    time.sleep(10)
    page_source = browser.page_source
    soup2 = BeautifulSoup(page_source, 'lxml')
    tags2 = soup2.find_all(text=re.compile("\$.*"))

def BTC_short_position_3x_8hrSMA():
#Hedging Short Position 8h SMA
    collected_data = [0]
    collected_data2 = [0]
    counter = 0
    initial_position = 100

    while True:
        PATH = '/Users/danielchen/Desktop/chromedriver'
        browser = webdriver.Chrome(PATH)
        sttime = d.now().strftime('%Y%m%d_%H:%M:%S ,')
        urlv2 = "https://pools.tracer.finance/trade/"
        browser.get(urlv2)
        time.sleep(10)
        page_source = browser.page_source
        soup2 = BeautifulSoup(page_source, 'lxml')
        tags2 = soup2.find_all(text=re.compile("\$.*"))
        crypto_tvlv2 = {'Bitcoin Spot': '', '3-BTC-Spot-Index': '', '3-BTC-SMA-Index': '', '3-BTC-SMA-LONGTVL': '',
                    '3-BTC-SMA-SHORTTVL': '', '3-BTC-SMA-LONGSKEW': '', '3-BTC-SMA-SHORTSKEW': '',
                    '3-BTC-SMA-LONGTRACER': '', '3-BTC-SMA-SHORTTRACER': '', '3-BTC-SMA-LONGBALANCER': '',
                    '3-BTC-SMA-SHORTBALANCER': ''}

        crypto_tvlv2['Bitcoin Spot'] = Decimal(sub(r'[^\d.]', '', tags2[0]))
        crypto_tvlv2['3-BTC-Spot-Index'] = Decimal(sub(r'[^\d.]', '', tags2[2]))
        crypto_tvlv2['3-BTC-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[10]))
        crypto_tvlv2['3-BTC-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[12]))
        crypto_tvlv2['3-BTC-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[15]))
        # Effective Leverage
        crypto_tvlv2['3-BTC-SMA-SHORTSKEW'] = round(3 * crypto_tvlv2['3-BTC-SMA-LONGTVL'] / crypto_tvlv2['3-BTC-SMA-SHORTTVL'], 3)
        crypto_tvlv2['3-BTC-SMA-LONGSKEW'] = round(3 * crypto_tvlv2['3-BTC-SMA-SHORTTVL'] / crypto_tvlv2['3-BTC-SMA-LONGTVL'], 3)
        crypto_tvlv2['3-BTC-SMA-LONGTRACER'] = Decimal(sub(r'[^\d.]', '', tags2[13]))
        crypto_tvlv2['3-BTC-SMA-SHORTTRACER'] = Decimal(sub(r'[^\d.]', '', tags2[16]))
        crypto_tvlv2['3-BTC-SMA-LONGBALANCER'] = Decimal(sub(r'[^\d.]', '', tags2[14]))
        crypto_tvlv2['3-BTC-SMA-SHORTBALANCER'] = Decimal(sub(r'[^\d.]', '', tags2[17]))
        r = requests.get("https://pools.tracer.finance/trade/")
        #value = r.text.strip() if r.status_code == 200 else '-1000'
        collected_data.append(float(sub(r'[^\d.]', '', tags2[10])))
        collected_data2.append(float(sub(r'[^\d.]', '', tags2[0])))
        SMA_price_difference = abs(collected_data[counter+1] - collected_data[counter])
        BTC_price_difference = abs(collected_data2[counter+1] - collected_data2[counter])
        #SMA_price_difference = randint(10,15)
        #BTC_price_difference = randint(5,20)
        print("3-BTC-8h-SMA-short")
        print("3-8hSMA")
        print((float(sub(r'[^\d.]', '', tags2[0]))))
        print("BTC")
        print((float(sub(r'[^\d.]', '', tags2[10]))))
        counter = counter + 1
        if SMA_price_difference != 0 and BTC_price_difference != 0:
            profit = SMA_price_difference * ((initial_position) / (float(sub(r'[^\d.]', '', tags2[10])))) * (float
                (crypto_tvlv2['3-BTC-SMA-SHORTSKEW']))
            hedge_position = profit * (float(sub(r'[^\d.]', '', tags2[0]))) / BTC_price_difference
            print(profit)
            # Amount of BTC to long in USD to hedge a short position in 8h SMA
            print("Amount to put into hedge position:" + str(hedge_position))

        else:
            print("NO PRICE CHANGE")
        time.sleep(3600)

def BTC_long_position_3x_8hrSMA():
#Hedging Long Position 8h SMA
    collected_data = [0]
    collected_data2 = [0]
    counter = 0
    initial_position = 100

    while True:
        PATH = '/Users/danielchen/Desktop/chromedriver'
        browser = webdriver.Chrome(PATH)
        sttime = d.now().strftime('%Y%m%d_%H:%M:%S ,')
        urlv2 = "https://pools.tracer.finance/trade/"
        browser.get(urlv2)
        time.sleep(10)
        page_source = browser.page_source
        soup2 = BeautifulSoup(page_source, 'lxml')
        tags2 = soup2.find_all(text=re.compile("\$.*"))
        crypto_tvlv2 = {'Bitcoin Spot': '', '3-BTC-Spot-Index': '', '3-BTC-SMA-Index': '', '3-BTC-SMA-LONGTVL': '',
                    '3-BTC-SMA-SHORTTVL': '', '3-BTC-SMA-LONGSKEW': '', '3-BTC-SMA-SHORTSKEW': '',
                    '3-BTC-SMA-LONGTRACER': '', '3-BTC-SMA-SHORTTRACER': '', '3-BTC-SMA-LONGBALANCER': '',
                    '3-BTC-SMA-SHORTBALANCER': ''}

        crypto_tvlv2['Bitcoin Spot'] = Decimal(sub(r'[^\d.]', '', tags2[0]))
        crypto_tvlv2['3-BTC-Spot-Index'] = Decimal(sub(r'[^\d.]', '', tags2[2]))
        crypto_tvlv2['3-BTC-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[10]))
        crypto_tvlv2['3-BTC-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[12]))
        crypto_tvlv2['3-BTC-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[15]))
        # Effective Leverage
        crypto_tvlv2['3-BTC-SMA-SHORTSKEW'] = round(3 * crypto_tvlv2['3-BTC-SMA-LONGTVL'] / crypto_tvlv2['3-BTC-SMA-SHORTTVL'],3)
        crypto_tvlv2['3-BTC-SMA-LONGSKEW'] = round(3 * crypto_tvlv2['3-BTC-SMA-SHORTTVL'] / crypto_tvlv2['3-BTC-SMA-LONGTVL'],3)
        crypto_tvlv2['3-BTC-SMA-LONGTRACER'] = Decimal(sub(r'[^\d.]', '', tags2[13]))
        crypto_tvlv2['3-BTC-SMA-SHORTTRACER'] = Decimal(sub(r'[^\d.]', '', tags2[16]))
        crypto_tvlv2['3-BTC-SMA-LONGBALANCER'] = Decimal(sub(r'[^\d.]', '', tags2[14]))
        crypto_tvlv2['3-BTC-SMA-SHORTBALANCER'] = Decimal(sub(r'[^\d.]', '', tags2[17]))
        r = requests.get("https://pools.tracer.finance/trade/")
        #value = r.text.strip() if r.status_code == 200 else '-1000'
        collected_data.append(float(sub(r'[^\d.]', '', tags2[10])))
        collected_data2.append(float(sub(r'[^\d.]', '', tags2[0])))
        SMA_price_difference = abs(collected_data[counter+1] - collected_data[counter])
        BTC_price_difference = abs(collected_data2[counter+1] - collected_data2[counter])
        #SMA_price_difference = randint(10,15)
        #BTC_price_difference = randint(5,20)
        print("3-BTC-8h-SMA-long")
        print("3-8hSMA")
        print((float(sub(r'[^\d.]', '', tags2[10]))))
        print("BTC")
        print((float(sub(r'[^\d.]', '', tags2[0]))))
        counter = counter + 1
        if SMA_price_difference != 0 and BTC_price_difference != 0:
            profit = SMA_price_difference * ((initial_position) / (float(sub(r'[^\d.]', '', tags2[10])))) * (float
                (crypto_tvlv2['3-BTC-SMA-LONGSKEW']))
            hedge_position = profit * (float(sub(r'[^\d.]', '', tags2[0]))) / BTC_price_difference
            print(profit)
            # Amount of BTC to short in USD to hedge a long position in 8h SMA
            print("Amount to put into hedge position:" + str(hedge_position))

        else:
            print("NO PRICE CHANGE")
        time.sleep(3600)

def ETH_short_position_10x_8hrSMA():
#Hedging Short Position 8h SMA
    collected_data = [0]
    collected_data2 = [0]
    counter = 0
    initial_position = 100

    while True:
        PATH = '/Users/danielchen/Desktop/chromedriver'
        browser = webdriver.Chrome(PATH)
        sttime = d.now().strftime('%Y%m%d_%H:%M:%S ,')
        urlv2 = "https://pools.tracer.finance/trade/"
        browser.get(urlv2)
        time.sleep(10)
        page_source = browser.page_source
        soup2 = BeautifulSoup(page_source, 'lxml')
        tags2 = soup2.find_all(text=re.compile("\$.*"))
        crypto_tvlv2 = {'Ethereum Spot': '', 'ETH-10x-Index': '', '3-ETH-SMA-Index': '', '3-ETH-SMA-LONGTVL': '',
                        '3-ETH-SMA-SHORTTVL': '', '3-ETH-SMA-LONGSKEW': '', '3-ETH-SMA-SHORTSKEW': '',
                        '3-ETH-SMA-LONGTRACER': '', '3-ETH-SMA-SHORTTRACER': '', '3-ETH-SMA-LONGBALANCER': '',
                        '3-ETH-SMA-SHORTBALANCER': '', '10-ETH-SMA-LONGTVL': '', '10-ETH-SMA-SHORTTVL': '',
                        '10-ETH-SMA-SHORTSKEW': '', '10-ETH-SMA-LONGSKEW': ''}

        crypto_tvlv2['Ethereum Spot'] = Decimal(sub(r'[^\d.]', '', tags2[18]))
        crypto_tvlv2['3-ETH-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[26]))
        crypto_tvlv2['3-ETH-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[28]))
        crypto_tvlv2['3-ETH-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[31]))
        crypto_tvlv2['3-ETH-SMA-SHORTSKEW'] = round(
            3 * crypto_tvlv2['3-ETH-SMA-LONGTVL'] / crypto_tvlv2['3-ETH-SMA-SHORTTVL'], 3)
        crypto_tvlv2['3-ETH-SMA-LONGSKEW'] = round(
            3 * crypto_tvlv2['3-ETH-SMA-SHORTTVL'] / crypto_tvlv2['3-ETH-SMA-LONGTVL'], 3)
        crypto_tvlv2['10-ETH-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[20]))
        crypto_tvlv2['10-ETH-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[22]))
        crypto_tvlv2['10-ETH-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[24]))
        crypto_tvlv2['10-ETH-SMA-SHORTSKEW'] = round(
            10 * crypto_tvlv2['10-ETH-SMA-LONGTVL'] / crypto_tvlv2['10-ETH-SMA-SHORTTVL'], 3)
        crypto_tvlv2['10-ETH-SMA-LONGSKEW'] = round(
            10 * crypto_tvlv2['10-ETH-SMA-SHORTTVL'] / crypto_tvlv2['10-ETH-SMA-LONGTVL'], 3)
        r = requests.get("https://pools.tracer.finance/trade/")
        #value = r.text.strip() if r.status_code == 200 else '-1000'
        collected_data.append(float(sub(r'[^\d.]', '', tags2[20])))
        collected_data2.append(float(sub(r'[^\d.]', '', tags2[18])))
        SMA_price_difference = abs(collected_data[counter+1] - collected_data[counter])
        ETH_price_difference = abs(collected_data2[counter+1] - collected_data2[counter])
        #SMA_price_difference = randint(10, 15)
        #ETH_price_difference = randint(5, 20)
        print("10-ETH-8h-SMA-short")
        print(SMA_price_difference)
        print(ETH_price_difference)
        print("10-8hSMA")
        print((float(sub(r'[^\d.]', '', tags2[20]))))
        print("ETH")
        print((float(sub(r'[^\d.]', '', tags2[18]))))
        counter = counter + 1
        print(float(crypto_tvlv2['10-ETH-SMA-SHORTSKEW']))
        if SMA_price_difference != 0 and ETH_price_difference != 0:
            profit = SMA_price_difference * ((initial_position) / (float(sub(r'[^\d.]', '', tags2[20])))) * (float(crypto_tvlv2['10-ETH-SMA-SHORTSKEW']))
            hedge_position = profit * (float(sub(r'[^\d.]', '', tags2[18]))) / ETH_price_difference
            print(profit)
            # Amount of ETH to long in USD to hedge a short position in 8h SMA
            print("Amount to put into hedge position:" + str(hedge_position))

        else:
            print("NO PRICE CHANGE")
        time.sleep(3600)

def ETH_long_position_10x_8hrSMA():
#Hedging long Position 8h SMA
    collected_data = [0]
    collected_data2 = [0]
    counter = 0
    initial_position = 100

    while True:
        PATH = '/Users/danielchen/Desktop/chromedriver'
        browser = webdriver.Chrome(PATH)
        sttime = d.now().strftime('%Y%m%d_%H:%M:%S ,')
        urlv2 = "https://pools.tracer.finance/trade/"
        browser.get(urlv2)
        time.sleep(10)
        page_source = browser.page_source
        soup2 = BeautifulSoup(page_source, 'lxml')
        tags2 = soup2.find_all(text=re.compile("\$.*"))
        crypto_tvlv2 = {'Ethereum Spot': '', 'ETH-10x-Index': '', '3-ETH-SMA-Index': '', '3-ETH-SMA-LONGTVL': '',
                        '3-ETH-SMA-SHORTTVL': '', '3-ETH-SMA-LONGSKEW': '', '3-ETH-SMA-SHORTSKEW': '',
                        '3-ETH-SMA-LONGTRACER': '', '3-ETH-SMA-SHORTTRACER': '', '3-ETH-SMA-LONGBALANCER': '',
                        '3-ETH-SMA-SHORTBALANCER': '', '10-ETH-SMA-LONGTVL': '', '10-ETH-SMA-SHORTTVL': '',
                        '10-ETH-SMA-SHORTSKEW': '', '10-ETH-SMA-LONGSKEW': ''}

        crypto_tvlv2['Ethereum Spot'] = Decimal(sub(r'[^\d.]', '', tags2[18]))
        crypto_tvlv2['3-ETH-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[26]))
        crypto_tvlv2['3-ETH-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[28]))
        crypto_tvlv2['3-ETH-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[31]))
        crypto_tvlv2['3-ETH-SMA-SHORTSKEW'] = round(3 * crypto_tvlv2['3-ETH-SMA-LONGTVL'] / crypto_tvlv2['3-ETH-SMA-SHORTTVL'], 3)
        crypto_tvlv2['3-ETH-SMA-LONGSKEW'] = round(3 * crypto_tvlv2['3-ETH-SMA-SHORTTVL'] / crypto_tvlv2['3-ETH-SMA-LONGTVL'], 3)
        crypto_tvlv2['10-ETH-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[20]))
        crypto_tvlv2['10-ETH-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[22]))
        crypto_tvlv2['10-ETH-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[24]))
        crypto_tvlv2['10-ETH-SMA-SHORTSKEW'] = round(10 * crypto_tvlv2['10-ETH-SMA-LONGTVL'] / crypto_tvlv2['10-ETH-SMA-SHORTTVL'], 3)
        crypto_tvlv2['10-ETH-SMA-LONGSKEW'] = round(10 * crypto_tvlv2['10-ETH-SMA-SHORTTVL'] / crypto_tvlv2['10-ETH-SMA-LONGTVL'], 3)
        r = requests.get("https://pools.tracer.finance/trade/")
        #value = r.text.strip() if r.status_code == 200 else '-1000'
        collected_data.append(float(sub(r'[^\d.]', '', tags2[20])))
        collected_data2.append(float(sub(r'[^\d.]', '', tags2[18])))
        SMA_price_difference = abs(collected_data[counter+1] - collected_data[counter])
        ETH_price_difference = abs(collected_data2[counter+1] - collected_data2[counter])
        #SMA_price_difference = randint(10, 15)
        #ETH_price_difference = randint(5, 20)
        print("10-ETH-8h-SMA-long")
        print(SMA_price_difference)
        print(ETH_price_difference)
        print("10-8hSMA")
        print((float(sub(r'[^\d.]', '', tags2[20]))))
        print("ETH")
        print((float(sub(r'[^\d.]', '', tags2[18]))))
        counter = counter + 1
        print(float(crypto_tvlv2['10-ETH-SMA-LONGSKEW']))
        if SMA_price_difference != 0 and ETH_price_difference != 0:
            profit = SMA_price_difference * ((initial_position) / (float(sub(r'[^\d.]', '', tags2[20])))) * (float(crypto_tvlv2['10-ETH-SMA-LONGSKEW']))
            hedge_position = profit * (float(sub(r'[^\d.]', '', tags2[18]))) / ETH_price_difference
            print(profit)
            # Amount of ETH to short in USD to hedge a long position in 8h SMA
            print("Amount to put into hedge position:" + str(hedge_position))

        else:
            print("NO PRICE CHANGE")
        time.sleep(3600)

def ETH_short_position_3_8hrSMA():
#Hedging Short Position 8h SMA
    collected_data = [0]
    collected_data2 = [0]
    counter = 0
    initial_position = 100

    while True:
        PATH = '/Users/danielchen/Desktop/chromedriver'
        browser = webdriver.Chrome(PATH)
        sttime = d.now().strftime('%Y%m%d_%H:%M:%S ,')
        urlv2 = "https://pools.tracer.finance/trade/"
        browser.get(urlv2)
        time.sleep(10)
        page_source = browser.page_source
        soup2 = BeautifulSoup(page_source, 'lxml')
        tags2 = soup2.find_all(text=re.compile("\$.*"))
        crypto_tvlv2 = {'Ethereum Spot': '', 'ETH-10x-Index': '', '3-ETH-SMA-Index': '', '3-ETH-SMA-LONGTVL': '',
                        '3-ETH-SMA-SHORTTVL': '', '3-ETH-SMA-LONGSKEW': '', '3-ETH-SMA-SHORTSKEW': '',
                        '3-ETH-SMA-LONGTRACER': '', '3-ETH-SMA-SHORTTRACER': '', '3-ETH-SMA-LONGBALANCER': '',
                        '3-ETH-SMA-SHORTBALANCER': '', '10-ETH-SMA-LONGTVL': '', '10-ETH-SMA-SHORTTVL': '',
                        '10-ETH-SMA-SHORTSKEW': '', '10-ETH-SMA-LONGSKEW': ''}

        crypto_tvlv2['Ethereum Spot'] = Decimal(sub(r'[^\d.]', '', tags2[18]))
        crypto_tvlv2['3-ETH-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[26]))
        crypto_tvlv2['3-ETH-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[28]))
        crypto_tvlv2['3-ETH-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[31]))
        crypto_tvlv2['3-ETH-SMA-SHORTSKEW'] = round(3 * crypto_tvlv2['3-ETH-SMA-LONGTVL'] / crypto_tvlv2['3-ETH-SMA-SHORTTVL'], 3)
        crypto_tvlv2['3-ETH-SMA-LONGSKEW'] = round(3 * crypto_tvlv2['3-ETH-SMA-SHORTTVL'] / crypto_tvlv2['3-ETH-SMA-LONGTVL'], 3)
        crypto_tvlv2['10-ETH-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[20]))
        crypto_tvlv2['10-ETH-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[22]))
        crypto_tvlv2['10-ETH-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[24]))
        crypto_tvlv2['10-ETH-SMA-SHORTSKEW'] = round(10 * crypto_tvlv2['10-ETH-SMA-LONGTVL'] / crypto_tvlv2['10-ETH-SMA-SHORTTVL'], 3)
        crypto_tvlv2['10-ETH-SMA-LONGSKEW'] = round(10 * crypto_tvlv2['10-ETH-SMA-SHORTTVL'] / crypto_tvlv2['10-ETH-SMA-LONGTVL'], 3)
        r = requests.get("https://pools.tracer.finance/trade/")
        #value = r.text.strip() if r.status_code == 200 else '-1000'
        collected_data.append(float(sub(r'[^\d.]', '', tags2[26])))
        collected_data2.append(float(sub(r'[^\d.]', '', tags2[18])))
        SMA_price_difference = abs(collected_data[counter+1] - collected_data[counter])
        ETH_price_difference = abs(collected_data2[counter+1] - collected_data2[counter])
        #SMA_price_difference = randint(10, 15)
        #ETH_price_difference = randint(5, 20)
        print("3-ETH-8h-SMA-short")
        print(SMA_price_difference)
        print(ETH_price_difference)
        print("3-8hSMA")
        print((float(sub(r'[^\d.]', '', tags2[26]))))
        print("ETH")
        print((float(sub(r'[^\d.]', '', tags2[18]))))
        counter = counter + 1
        print(float(crypto_tvlv2['3-ETH-SMA-SHORTSKEW']))
        if SMA_price_difference != 0 and ETH_price_difference != 0:
            profit = SMA_price_difference * ((initial_position) / (float(sub(r'[^\d.]', '', tags2[26])))) * (float(crypto_tvlv2['3-ETH-SMA-SHORTSKEW']))
            hedge_position = profit * (float(sub(r'[^\d.]', '', tags2[18]))) / ETH_price_difference
            print(profit)
            # Amount of ETH to long in USD to hedge a short position in 8h SMA
            print("Amount to put into hedge position:" + str(hedge_position))

        else:
            print("NO PRICE CHANGE")
        time.sleep(3600)

def ETH_long_position_3_8hrSMA():
#Hedging Short Position 8h SMA
    collected_data = [0]
    collected_data2 = [0]
    counter = 0
    initial_position = 100

    while True:
        PATH = '/Users/danielchen/Desktop/chromedriver'
        browser = webdriver.Chrome(PATH)
        sttime = d.now().strftime('%Y%m%d_%H:%M:%S ,')
        urlv2 = "https://pools.tracer.finance/trade/"
        browser.get(urlv2)
        time.sleep(10)
        page_source = browser.page_source
        soup2 = BeautifulSoup(page_source, 'lxml')
        tags2 = soup2.find_all(text=re.compile("\$.*"))
        crypto_tvlv2 = {'Ethereum Spot': '', 'ETH-10x-Index': '', '3-ETH-SMA-Index': '', '3-ETH-SMA-LONGTVL': '',
                        '3-ETH-SMA-SHORTTVL': '', '3-ETH-SMA-LONGSKEW': '', '3-ETH-SMA-SHORTSKEW': '',
                        '3-ETH-SMA-LONGTRACER': '', '3-ETH-SMA-SHORTTRACER': '', '3-ETH-SMA-LONGBALANCER': '',
                        '3-ETH-SMA-SHORTBALANCER': '', '10-ETH-SMA-LONGTVL': '', '10-ETH-SMA-SHORTTVL': '',
                        '10-ETH-SMA-SHORTSKEW': '', '10-ETH-SMA-LONGSKEW': ''}

        crypto_tvlv2['Ethereum Spot'] = Decimal(sub(r'[^\d.]', '', tags2[18]))
        crypto_tvlv2['3-ETH-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[26]))
        crypto_tvlv2['3-ETH-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[28]))
        crypto_tvlv2['3-ETH-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[31]))
        crypto_tvlv2['3-ETH-SMA-SHORTSKEW'] = round(3 * crypto_tvlv2['3-ETH-SMA-LONGTVL'] / crypto_tvlv2['3-ETH-SMA-SHORTTVL'], 3)
        crypto_tvlv2['3-ETH-SMA-LONGSKEW'] = round(3 * crypto_tvlv2['3-ETH-SMA-SHORTTVL'] / crypto_tvlv2['3-ETH-SMA-LONGTVL'], 3)
        crypto_tvlv2['10-ETH-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[20]))
        crypto_tvlv2['10-ETH-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[22]))
        crypto_tvlv2['10-ETH-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[24]))
        crypto_tvlv2['10-ETH-SMA-SHORTSKEW'] = round(10 * crypto_tvlv2['10-ETH-SMA-LONGTVL'] / crypto_tvlv2['10-ETH-SMA-SHORTTVL'], 3)
        crypto_tvlv2['10-ETH-SMA-LONGSKEW'] = round(10 * crypto_tvlv2['10-ETH-SMA-SHORTTVL'] / crypto_tvlv2['10-ETH-SMA-LONGTVL'], 3)
        r = requests.get("https://pools.tracer.finance/trade/")
        #value = r.text.strip() if r.status_code == 200 else '-1000'
        collected_data.append(float(sub(r'[^\d.]', '', tags2[26])))
        collected_data2.append(float(sub(r'[^\d.]', '', tags2[18])))
        SMA_price_difference = abs(collected_data[counter+1] - collected_data[counter])
        ETH_price_difference = abs(collected_data2[counter+1] - collected_data2[counter])
        #SMA_price_difference = randint(10, 15)
        #ETH_price_difference = randint(5, 20)
        print("3-ETH-8h-SMA-long")
        print(SMA_price_difference)
        print(ETH_price_difference)
        print("3-8hSMA")
        print((float(sub(r'[^\d.]', '', tags2[26]))))
        print("ETH")
        print((float(sub(r'[^\d.]', '', tags2[18]))))
        counter = counter + 1
        print(float(crypto_tvlv2['3-ETH-SMA-LONGSKEW']))
        if SMA_price_difference != 0 and ETH_price_difference != 0:
            profit = SMA_price_difference * ((initial_position) / (float(sub(r'[^\d.]', '', tags2[26])))) * (float(crypto_tvlv2['3-ETH-SMA-LONGSKEW']))
            hedge_position = profit * (float(sub(r'[^\d.]', '', tags2[18]))) / ETH_price_difference
            print(profit)
            # Amount of ETH to short in USD to hedge a long position in 8h SMA
            print("Amount to put into hedge position:" + str(hedge_position))

        else:
            print("NO PRICE CHANGE")
        time.sleep(3600)


def WTI_short_position_3_8hrSMA():
#Hedging Short Position 8h SMA
    collected_data = [0]
    collected_data2 = [0]
    counter = 0
    initial_position = 100

    while True:
        PATH = '/Users/danielchen/Desktop/chromedriver'
        browser = webdriver.Chrome(PATH)
        sttime = d.now().strftime('%Y%m%d_%H:%M:%S ,')
        urlv2 = "https://pools.tracer.finance/trade/"
        browser.get(urlv2)
        time.sleep(10)
        page_source = browser.page_source
        soup2 = BeautifulSoup(page_source, 'lxml')
        tags2 = soup2.find_all(text=re.compile("\$.*"))
        crypto_tvlv2 = {'WTI Spot': '', '3-WTI-SMA-Index': '', '3-WTI-SMA-LONGTVL': '', '3-WTI-SMA-SHORTTVL': '',
                        '3-WTI-SMA-SHORTSKEW': '', '3-WTI-SMA-LONGSKEW': ''}

        crypto_tvlv2['WTI Spot'] = Decimal(sub(r'[^\d.]', '', tags2[34]))
        crypto_tvlv2['3-WTI-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[36]))
        crypto_tvlv2['3-WTI-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[38]))
        crypto_tvlv2['3-WTI-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[41]))
        # Effective Leverage
        crypto_tvlv2['3-WTI-SMA-SHORTSKEW'] = round(3 * crypto_tvlv2['3-WTI-SMA-LONGTVL'] / crypto_tvlv2['3-WTI-SMA-SHORTTVL'], 3)
        crypto_tvlv2['3-WTI-SMA-LONGSKEW'] = round(3 * crypto_tvlv2['3-WTI-SMA-SHORTTVL'] / crypto_tvlv2['3-WTI-SMA-LONGTVL'], 3)
        r = requests.get("https://pools.tracer.finance/trade/")
        #value = r.text.strip() if r.status_code == 200 else '-1000'
        collected_data.append(float(sub(r'[^\d.]', '', tags2[36])))
        collected_data2.append(float(sub(r'[^\d.]', '', tags2[34])))
        SMA_price_difference = abs(collected_data[counter+1] - collected_data[counter])
        WTI_price_difference = abs(collected_data2[counter+1] - collected_data2[counter])
        #SMA_price_difference = randint(10, 15)
        #WTI_price_difference = randint(5, 20)
        print("3-WTI-8h-SMA-short")
        print(SMA_price_difference)
        print(WTI_price_difference)
        print("3-8hSMA")
        print((float(sub(r'[^\d.]', '', tags2[36]))))
        print("WTI")
        print((float(sub(r'[^\d.]', '', tags2[34]))))
        counter = counter + 1
        print(float(crypto_tvlv2['3-WTI-SMA-SHORTSKEW']))
        if SMA_price_difference != 0 and WTI_price_difference != 0:
            profit = SMA_price_difference * ((initial_position) / (float(sub(r'[^\d.]', '', tags2[36])))) * (float(crypto_tvlv2['3-WTI-SMA-SHORTSKEW']))
            hedge_position = profit * (float(sub(r'[^\d.]', '', tags2[34]))) / WTI_price_difference
            print(profit)
            # Amount of WTI to long in USD to hedge a short position in 8h SMA
            print("Amount to put into hedge position:" + str(hedge_position))

        else:
            print("NO PRICE CHANGE")
        time.sleep(3600)

def WTI_long_position_3_8hrSMA():
#Hedging Short Position 8h SMA
    collected_data = [0]
    collected_data2 = [0]
    counter = 0
    initial_position = 100

    while True:
        PATH = '/Users/danielchen/Desktop/chromedriver'
        browser = webdriver.Chrome(PATH)
        sttime = d.now().strftime('%Y%m%d_%H:%M:%S ,')
        urlv2 = "https://pools.tracer.finance/trade/"
        browser.get(urlv2)
        time.sleep(10)
        page_source = browser.page_source
        soup2 = BeautifulSoup(page_source, 'lxml')
        tags2 = soup2.find_all(text=re.compile("\$.*"))
        crypto_tvlv2 = {'WTI Spot': '', '3-WTI-SMA-Index': '', '3-WTI-SMA-LONGTVL': '', '3-WTI-SMA-SHORTTVL': '',
                        '3-WTI-SMA-SHORTSKEW': '', '3-WTI-SMA-LONGSKEW': ''}
        crypto_tvlv2['WTI Spot'] = Decimal(sub(r'[^\d.]', '', tags2[34]))
        crypto_tvlv2['3-WTI-SMA-Index'] = Decimal(sub(r'[^\d.]', '', tags2[36]))
        crypto_tvlv2['3-WTI-SMA-LONGTVL'] = Decimal(sub(r'[^\d.]', '', tags2[38]))
        crypto_tvlv2['3-WTI-SMA-SHORTTVL'] = Decimal(sub(r'[^\d.]', '', tags2[41]))
        # Effective Leverage
        crypto_tvlv2['3-WTI-SMA-SHORTSKEW'] = round(3 * crypto_tvlv2['3-WTI-SMA-LONGTVL'] / crypto_tvlv2['3-WTI-SMA-SHORTTVL'], 3)
        crypto_tvlv2['3-WTI-SMA-LONGSKEW'] = round(3 * crypto_tvlv2['3-WTI-SMA-SHORTTVL'] / crypto_tvlv2['3-WTI-SMA-LONGTVL'], 3)
        r = requests.get("https://pools.tracer.finance/trade/")
        #value = r.text.strip() if r.status_code == 200 else '-1000'
        collected_data.append(float(sub(r'[^\d.]', '', tags2[36])))
        collected_data2.append(float(sub(r'[^\d.]', '', tags2[34])))
        SMA_price_difference = abs(collected_data[counter+1] - collected_data[counter])
        WTI_price_difference = abs(collected_data2[counter+1] - collected_data2[counter])
        #SMA_price_difference = randint(10, 15)
        #WTI_price_difference = randint(5, 20)
        print("3-WTI-8h-SMA-long")
        print(SMA_price_difference)
        print(WTI_price_difference)
        print("3-8hSMA")
        print((float(sub(r'[^\d.]', '', tags2[36]))))
        print("WTI")
        print((float(sub(r'[^\d.]', '', tags2[34]))))
        counter = counter + 1
        print(float(crypto_tvlv2['3-WTI-SMA-LONGSKEW']))
        if SMA_price_difference != 0 and WTI_price_difference != 0:
            profit = SMA_price_difference * ((initial_position) / (float(sub(r'[^\d.]', '', tags2[36])))) * (float(crypto_tvlv2['3-WTI-SMA-LONGSKEW']))
            hedge_position = profit * (float(sub(r'[^\d.]', '', tags2[34]))) / WTI_price_difference
            print(profit)
            # Amount of WTI to short in USD to hedge a long position in 8h SMA
            print("Amount to put into hedge position:" + str(hedge_position))

        else:
            print("NO PRICE CHANGE")
        time.sleep(3600)

BTC_short_position_3x_8hrSMA()

BTC_long_position_3x_8hrSMA()

ETH_short_position_10x_8hrSMA()

ETH_long_position_10x_8hrSMA()

ETH_short_position_3_8hrSMA()

ETH_long_position_3_8hrSMA()

WTI_short_position_3_8hrSMA()

WTI_long_position_3_8hrSMA()

