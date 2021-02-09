import sys
import re
import os
import urllib.request

#scraping library
from bs4 import BeautifulSoup


#Tor connection protocol - stem lib
from stem import Signal
from stem.control import Controller
from toripchanger import TorIpChanger

import socks
import socket


#Initiating connection - New IP at each connection by default
with Controller.from_port(port=9051) as controller:
    try:
        controller.authenticate("16:01EECDB19AF14C9F609B57C95E8E2EECFB8FC5862E64F543188A4DE2DB")
    except Exception as e:
        print("""Error in connection, link is probably dead""")
    else:
        print("Authentication succeeded")

    controller.signal(Signal.NEWNYM)
    print("New TOR connection processed")

#TOR-Config
SOCKS_PORT = 9050
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", SOCKS_PORT)
socket.socket = socks.socksocket




#DNS-Resolution
def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

socket.getaddrinfo = getaddrinfo


#Scrapping Onion links.
def scrape(url, timeout_value = 10, verbose=False, dataframe_storage = True):
    """
    Core function : Scrape URL HTML content using bs4
    Store it in pandas Dataframe ready to use for machine learning classification
    -------------------------------------------------
    url : onion hidden service
    timeout : default value 60000ms - can be larger for onion services
    reuse_threshold : Inverse Renewal rate of IP , 0 means IP are always changed
    """

    timeout = timeout_value
    socket.setdefaulttimeout(timeout)

    #collecting html content.
    headers = {'User-Agent': 'Onion services scrapper | github.com/jct94/TorScrapper.git' }
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)

    #load response - print some info
    content = response.read()

    try:
        print("Including html tags, response has a length of {}".format(len(content)))
        if verbose == True:
            print(content)
    except ValueError:
        print("Scraping failed - It can be a dead link")
        pass

    #parse html response
    page = BeautifulSoup(content,'html.parser')

    #output id
    id = re.sub(r'[^\w]', '', url[5:])
    name = os.path.abspath("") + '/output/scraped-' + id + '.txt'
    #output saving
    file = open(name,'w')
    file.write(str(page.text))
    file.close()



if __name__=='__main__':

    if len(sys.argv) > 2:
        print(sys.argv)
        print('You have specified too many arguments')
        sys.exit()

    if len(sys.argv)==2:
        url=sys.argv[1]
        try:
            scrape(url)
        except ValueError:
            print("Invalid input")
