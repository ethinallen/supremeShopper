import os
import bs4
import time
import threading
import sys
import csv
import requests
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import checkStock

# TODO: give each driver a user agent

# the function a list of threads; start and join all of them
def startAndJoin(threads):
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

# returns our list of proxies
def getProxies():

    # empty list we are going to populate
    proxies = []

    # read in our proxies and return them
    with open('/users/drew/Projects/proxies/proxies.csv') as f:
        f = csv.reader(f)
        for elem in f:
            for proxy in elem:
                proxies.append(proxy)
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
        # going to combine these two lists into the dictionary
        self.listOfPaths = []
        self.listOfTexts = []
        # each text and path for every input field will become a dictionary for that field
        self.listOfDicts = []
        # self.createListOfDicts()

    # create our list of dictionaries; each dict corresponds to a field
    def createListOfDicts(self):
        self.listOfTexts.append()
        for i in range(0,len(self.listOfPaths)):
            self.listOfDicts.append({'path' : self.listOfPaths[i], 'text' : self.listOfTexts[i]})

    # create all of our driver instances
    def createAllDrivers(self):

        # create a driver instance and append make a dictionary of drivers and details
        def createDriver(proxy):

            # add options to our webdriver
            chrome_options = webdriver.ChromeOptions()
            # add the proxy to the driver
            chrome_options.add_argument('--proxy-server=http://%s' % proxy)
            # make the driver headless
            chrome_options.add_argument('headless')
            # make the driver
            driver = webdriver.Chrome(options=chrome_options, executable_path='/users/drew/Projects/drivers/chromedriver73/chromedriver')

            # that information to the dictionary of drivers
            self.driverList.append({'driver' : driver, 'proxy' : proxy})

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

        # create a list of threads (we are going to be doing that a lot)
        threads = [threading.Thread(target = createDriver, args = ((proxy,))) for proxy in self.proxyList]

        # start and join all of the threads
        startAndJoin(threads)

    # will test all of our proxies
    def testAllProxies(self):

        # test a singular proxy
        def testProxy(self, proxy):
            yield None

        yield None


    # will submit all of the fields on the page except for the exp date of cc
    # and the process payment button (becuase order matters)
    def clickAllButtons(self, listOfPaths):

        # will submit a single field on the page
        def clickButton(self, path, text):
            try:
                button = driver.find_element_by_xpath(path)
                button.send_keys(text)
            except Exception as e:
                print('FAILED TO SUBMIT WITH ERROR: {}'.format(e))
            return button

        # populate a list of threads
        threads = [threading.Thread(target=makeButton(), args=(dict[path], dict[text])) for dict in listOfDicts]

        # start and join all of the threads
        startAndJoin(threads)

if __name__ == '__main__':
    # create a bot instance
    bot = bot()
    # create all of the drivers
    bot.createAllDrivers()
    print(bot.driverList)
