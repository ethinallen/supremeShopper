from selenium import webdriver
import os
import requests
import bs4
import re
import time
import selenium.webdriver
import threading
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import checkStock

class bot():

    def __init__(self):

        # url that we are going to check
        self.checkURL = 'https://whatismyipaddress.com/'
        self.shopURL = 'https://supremenewyork.com/shop'
        self.proxyList = []
