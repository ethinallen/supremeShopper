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
        driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/users/drew/Projects/jubilantWaffle/chromedriver')
        self.driverDict[driver] = proxy

    # is going to test all of our proxies to make sure that they work
    def testProxies(self):
        # will write a function to check single proxies and then thread it to test all proxies
        return None

    # test our driver's proxy to make sure that it works
    def testDriver(driver):
        yield None
    # def
