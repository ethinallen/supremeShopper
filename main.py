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
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import checkStock
import RandomHeaders

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
        self.detailsList = []

    # create a driver instance and append make a dictionary of drivers and details
    def createDriver(self, proxy):
        # add options to our webdriver
        chrome_options = webdriver.ChromeOptions()
        # add the proxy to the driver
        chrome_options.add_argument('--proxy-server=http://%s' % proxy)
        # make the driver headless
        chrome_options.add_argument('headless')
        # give the driver a useragent
        header = RandomHeaders.LoadHeader()
        # make the driver
        driver = webdriver.Chrome(options=chrome_options, executable_path='/users/drew/Projects/drivers/chromedriver73/chromedriver')
        # eventually we are going to assign a header to the dirver and then add
        # that information to the dictionary of drivers
        self.detailsList.append({'driver' : driver, 'proxy' : proxy, 'header' : header})
        print('DRIVER INITIATED WITH PROXY {}'.format(proxy))

        try:
            driver.get('https://whatismyipaddress.com')
            time.sleep(60)
            ssName = str(proxy)
            ssName = ssName.strip(':') + '.png'
            driver.save_screenshot(ssName)
            driver.close()

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
    # def testProxy(self, proxy):
    #     # testing this url to make sure that the response code is <200>
    #     url = 'https://www.google.com'
    #     # make the request
    #     r = requests.get(url, proxy=proxy)
    #     return r.status_code

    # not going to use these functions right now because I can't issue a proxy
    # to requests
    # def testAllProxies(self):
    #     statusCodes = [self.testProxy(proxy) for proxy in self.proxyList]
    #     print(statusCodes)
    #     for i, code in enumerate(statusCodes):
    #         if code != 200:
    #             self.proxyList.pop(i)
    #     print()

    # test our driver's proxy to make sure that it works
    def testDriver(driver):
        yield None

if __name__ == '__main__':
    # create a bot instance
    bot = bot()
    # create all of the drivers
    bot.createAllDrivers()
    # bot.testAllProxies()
