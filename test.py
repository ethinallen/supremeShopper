## this is where i test all of my shit code
## before I put it in my other shit code

# from selenium import webdriver
#
# PROXY = '142.54.163.90:19006' # IP:PORT
#
# chrome_options = webdriver.Options()
# chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
#
# chrome = webdriver.Chrome(chrome_options=chrome_options, executable_path='/users/drew/Projects/drivers/chromedriver73/chromedriver' )
# chrome.get("http://whatismyipaddress.com")
#################
# I am an idiot hahahahahahaha
# import json
#
# with open('drew.drew') as data:
#     data = json.load(data)
#
# print(data['productType'])
#################
# import checkStock
#
# destinations = checkStock.main()
#################
import csv
import threading

proxies = []
with open('/users/drew/Projects/proxies/proxies.csv') as f:
    f = csv.reader(f)
    for elem in f:
        for proxy in elem:
            proxies.append(proxy)
# give us our proxies
list = [proxy for proxy in proxies]

def getThread(list):
