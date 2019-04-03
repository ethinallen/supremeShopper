from selenium import webdriver
import os
import requests
import bs4
import re
import time
import selenium.webdriver
import threading
import sys
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import checkStock

# returns our list of proxies
def getProxies():

    # empty list we are going to populate
    proxies = []

    # read in our proxies
    with open('/users/drew/Projects/proxies/proxies.csv') as f:
        f = csv.reader(f)
        for elem in f:
            for proxy in elem:
                proxies.append(proxy)
    # give us our proxies
    return proxies

class bot():

    def __init__(self):

        # url that we are going to check
        self.checkURL = 'https://whatismyipaddress.com/'
        self.shopURL = 'https://supremenewyork.com/shop'
        # our list of proxies
        self.proxyList = getProxies()
        # dictionary of every driver and its details
        self.driverDict = {}

    # create a driver instance and append make a dictionary of drivers and details
    def createDriver(self, proxy):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=http://%s' % proxy)
        driver = webdriver.Chrome(options=chrome_options, executable_path='/users/drew/Projects/drivers/chromedriver73/chromedriver')
        header = None
        self.driverDict[driver] = {'proxy' : proxy, 'header' : header}
        time.sleep(5)
        print('WE DID IT BOYS')
        driver.close()

    def createAllDrivers(self):

        # create a list of threads (we are going to be doing that a lot)
        threads = [threading.Thread(target = self.createDriver, args = (proxy,)) for proxy in self.proxyList]

        # # start and join all of the threads
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    # is going to test all of our proxies to make sure that they work
    def testProxies(self):
        # will write a function to check single proxies and then thread it to test all proxies
        yield None

    # test our driver's proxy to make sure that it works
    def testDriver(driver):
        yield None

if __name__ == '__main__':
    # create a bot instance
    bot = bot()
    # create all of the drivers
    bot.createAllDrivers()
    print(bot.driverDict)
