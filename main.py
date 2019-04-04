from selenium import webdriver
import os
import bs4
import re
import time
import selenium.webdriver
import threading
import sys
import csv
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import checkStock

# TODO: give each driver a user agent

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
        self.driverList = []
        # going to combine these two lists
        self.listOfPaths = []
        self.listOfTexts = []
        # each text and path for every input field will become a dictionary for that field
        self.listOfDicts = []

    # create our list of dictionaries; each dict corresponds to a field
    def createListOfDicts():
        listOfTexts.append()
        for i in range(0,len(listOfPaths)):
            listOfDicts.append({'path' : listOfPaths[i], 'text' : listOfTexts[i]})

    # create a driver instance and append make a dictionary of drivers and details
    def createDriver(self, proxy):
        # add options to our webdriver
        chrome_options = webdriver.ChromeOptions()
        # add the proxy to the driver
        chrome_options.add_argument('--proxy-server=http://%s' % proxy)
        # make the driver headless
        chrome_options.add_argument('headless')
        # make the driver
        driver = webdriver.Chrome(options=chrome_options, executable_path='/users/drew/Projects/drivers/chromedriver73/chromedriver')
        # eventually we are going to assign a header to the dirver and then add
        # that information to the dictionary of drivers
        self.driverList.append({'driver' : driver, 'proxy' : proxy, 'header' : header})
        print('DRIVER INITIATED WITH PROXY {}'.format(proxy))
        # try to get the page
        try:
            driver.get('https://whatismyipaddress.com')
            time.sleep(60)
            ssName = str(proxy)
            ssName = ssName.strip(':') + '.png'
            driver.save_screenshot(ssName)
            driver.close()

        # print the exception
        except Exception as e:
            print('DRIVER FAILED WITH EXCEPTION:    {}'.format(e))
            # closes the driver on exception
            driver.close()

    def createAllDrivers(self):

        # create a list of threads (we are going to be doing that a lot)
        threads = [threading.Thread(target = self.createDriver, args = (proxy,)) for proxy in self.proxyList]

        # start and join all of the threads
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    # is going to test all of our proxies to make sure that they work
    def testProxy(self, proxy):
        yield None

    # function to test all of my proxies and see their response code
    # will just be the threaded version of the testing of singular proxy
    def testAllProxies(self):
        yield None

    # will submit a single field on the page
    def clickButton(self, path, text):
        button = driver.find_element_by_xpath(path)
        button.send_keys(text)
        return button

    # will submit all of the fields on the page except for the exp date of cc
    # and the process payment button (becuase order matters)
    def clickAllButtons(self, listOfPaths):
        buttonList = [threading.Thread(target=makeButton(), args=(dict[path], dict[text])) for dict in listOfDicts]


if __name__ == '__main__':
    # create a bot instance
    bot = bot()
    # create all of the drivers
    bot.createAllDrivers()
    # bot.testAllProxies()
