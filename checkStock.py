import time, threading, requests, string, json
from bs4 import BeautifulSoup
from datetime import datetime

# read in all of our constants from details.json file
with open('details.json') as data:
    data = json.load(data)

# this is the type of product that we want to get
productType = data['productType']

# the name of the product that we are searching for
productKeyWord = data['productKeyWord']

# always check the checker
class checker:
    # check check check check check
    def __init__(self):
        self.destinations = []


# the base extension of the website domain that we are going to use
url = 'https://supremenewyork.com/shop'

# the string positions of the url extension
# sadd is to adjust for the length of the product
# type adding to the length of the url
sAdd = len(productType) * 2
staPos = 29 + sAdd
endPos = 38 + sAdd

# function to get the extensions to the url
def getExtensions(url):

    # make our request
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})

    # create soup instance
    soup = BeautifulSoup(r.text, features = 'html.parser')

    # makes a list of all of the extensions for the website that we need to visit
    extenList = []

    # makes a list of every full url that needs to be visited
    urlList = []

    # goes through every item of the type we want and
    # extracts the extension if it is a new item
    for a in soup.find_all('li', {'class' : productType }):
        for span in a.find_all('span', {'class' : 'new_item_tag'}):
            string = str(a)
            string = string[staPos:endPos]
            extenList.append(string)

    # populates the list of full urls that we need to go to
    for exten in extenList:
        fullPath = (url + '/' + productType + '/' + exten)
        urlList.append(fullPath)

    # returns the list of urls that we just found
    return urlList

# this is our function
def getName(url):

    # request the page and pull the title
    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    soup = BeautifulSoup(r.text, features = 'html.parser')
    title = str(soup.title)

    # make it all lowercase so that there's no canoodling
    # we do not like canoodling
    title = title.lower()

    # see if the name is in the title
    if productKeyWord in title:

        # assign the correct url to the checker's destination attribute
        checker.destinations.append(url)
        # return url

if __name__ == '__main__':

    # make a checker instance
    checker = checker()

    # say we are starting our program for the boys back home
    print('STARTING PROGRAM')

    # get our list of url's
    urlList = getExtensions(url)

    # create a list of threads
    threads = [threading.Thread(target = getName, args = (url,)) for url in urlList]

    # get our time so we can see how long the program takes
    t = time.time()

    # start all threads
    for thread in threads:
        thread.start()
    # join all threads
    for thread in threads:
        thread.join()

    # calculate how long it took to run the program
    t = time.time() - t

    # print the correct url of the page that we want
    for dest in checker.destinations:
        print('Found url: {}'.format(dest))

    # print our time
    print('Retreived in {} seconds.'.format(t))
