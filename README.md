# TorScrapper
A basic scrapper made in python with BeautifulSoup and Tor support to -

* Scrape hidden services - crawling functionality has not been included
* Save the output in html - Need some pre-processing to use it as a input for machine learning algorithm


## Basic setup

### Tor setup
Before you run the scrapper make sure the following things are done properly:

* Run tor service
`sudo service tor start`
or `brew services tor start` for MacOS users


* Set a password for tor
`tor --hash-password "my_password" ` and do not forget to include it in your python scripts

* Modify value in scrapper.py

* Go to /etc/tor/torrc and uncomment - _**ControlPort 9051**_ , you may consider accessing torrc config file using `sudo nano torrc` to be able to save it

### Privoxy setup

* Install privoxy
`sudo apt-get install privoxy`
or `brew install privoxy` for MacOS users


* Change your privoxy config to get access to Tor Network  
`cd /` to go to root directory then
`cd /etc/privoxy`  

* Open your config file  
`nano config`

* Uncomment following line  
`forward-socks5 / localhost:9050`

* Restart prixoxy to load changes
`sudo /etc/init.d/privoxy restart` or
`brew services restart privoxy`for MacOS users

### Deployment

* Create your virtualenv and install requirements by running the following commands :
`pip install virtualenv`  
`virtualenv yourenv`  
`source yourenv/bin/activate`   
`pip install -r requirements.txt`   


## Running

* Copy all the onion and normal links you want to scrape in _onions.txt_ - You can find onion hidden services by subscribing to Hunchly newsletter for example

```
[nano]/[vim]/[gedit]/[Your choice of editor] onions.txt
```

* Run Tthe scrapper using python3

```
python3 scrapper.py
```
```
Choose option number 2 if you want to run scraping engine
```

* Check the scraped outputs in output folder



## LICENSE

MIT LICENSE
