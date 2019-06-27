import os
import bs4
import time
import threading
import sys
import csv
import json
import requests
from datetime import datetime
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import checkStock

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
    with open('proxies.csv') as f:
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
        self.itemURL = None
        self.checkoutURL = 'https://supremenewyork.com/shop/cart'
        # our list of proxies
        self.proxyList = getProxies()
        # dictionary of every driver and its details
        self.driverList = []
        # going to combine these two lists into the dictionary
        self.listOfFields = []

    # create our list of dictionaries; each dict corresponds to a field
    def createListOfDicts(self):
        self.populateTexts()
        self.listOfTexts.append()
        for i in range(0,len(self.listOfTexts)):
            self.listOfDicts.append({'path' : self.listOfPaths[i], 'text' : self.listOfTexts[i]})
        print(listOfDicts)

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
            # give the driver a user Agent
            chrome_options.add_argument('user-agent = Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_0; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9')
            # make the driver
            driver = webdriver.Chrome(options=chrome_options, executable_path='/home/drew/projects/drivers/geckoedriver')

            # that information to the dictionary of drivers
            self.driverList.append({'driver' : driver, 'proxy' : proxy})

            print('DRIVER INITIATED WITH PROXY {}'.format(proxy))

            # try to get the page
            try:
                driver.get(self.shopURL)

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


    # will submit all of the fields on the page
    # and get us to the captcha
    def submitAllFields(self, driver):

        # I am going to write a much cleaner way to execute this later
        # but right now I am under the gun and I have no standards
        # the world can judge me for writing it this way idc :^)

        # read in our checkout paths from our json of paths
        with open('checkoutPaths.json') as data:
            data = json.load(data)
            data = data['checkout']

        # load all of my super secret payment information
        with open('payment.json') as data:
            drew = json.load(data)
            drew = data['drew']

        def submitInformation():

            for key in data:
                self.listOfFields.append({key: data[key]})

            def submitField(field):
                type = field['type']
                path = field['path']
                interaction = driver.find_element_by_xpath(path)

                if type == 'textEntry':
                    interaction.send_keys(drew[field])
                if type == 'dropdown':

                    yield None
                if type == 'button':
                    nameButton = driver.find_element_by_xpath(data['name'])
                    yield None

    # this is our 'final approach' function
    def finalApproach(self, driver):
        # get the url of the item that we want
        driver.get(self.itemURL)
        # add the item to our cart (i am going to clean this up later)
        checkout = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/fieldset[2]/input')
        checkout.click()
        driver.get(bot.checkoutURL)
        self.clickAllButtons(driver)

    # the main function of the bot
    def main(self):
        threads = [threading.Thread(target = self.finalApproach, args = (driver['driver'],)) for driver in self.driverList]
        startAndJoin(threads)

if __name__ == '__main__':
    # create a bot instance
    bot = bot()
    # create all of the drivers
    bot.createAllDrivers()

    print('CREATED ALL DRIVERS')

    bot.itemURL = checkStock.checkStock()

    print('FOUND URL {}'.format(bot.itemURL))

    bot.main()
