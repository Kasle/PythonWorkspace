import urlparse
import urllib
import re
from bs4 import BeautifulSoup
import requests
import sys

USER = 'Arkyd'
PASS = '8112151413714'
UNI = 's125-us.ogame.gameforge.com'

URL = 'http://us.ogame.gameforge.com/main/login'

def main():
    session = requests.session()

    login_data = {
        'kid': '',
        'login': USER,
        'pass': PASS,
        'uni': UNI,
    }

    # Authenticate
    r = session.post(URL, data=login_data)

    #Try accessing a page that requires you to be logged in
    r = session.post('http://s125-us.ogame.gameforge.com/game/index.php?page=research&deprecated=1')
    #r = session.post('http://s125-us.ogame.gameforge.com/game/index.php')
    #print r.params

    #data = [{'modus': '1','type': '115'}, {'modus': '1','type': '113'},]
    # = session.get('http://s125-us.ogame.gameforge.com/game/index.php?page=research&modus=1&type=115&menge=1')
    #r = session.post('http://s125-us.ogame.gameforge.com/game/index.php?page=research&deprecated=1', data=data[1])
    
if __name__ == '__main__':
    main()

'''import urlparse
import urllib
import re
from bs4 import BeautifulSoup

import time

url = 'https://en.wikipedia.org/wiki/Special:Random'

search = raw_input('Please enter search term: ')

urls = [url] #Current URLs
visited = [url] #Historic URLs

_br = False

with open("results.txt", "a") as myfile:

while len(urls) > 0:
    try:
        htmltext = urllib.urlopen(urls[0]).read()
    except:
        pass
    
    soup = BeautifulSoup(htmltext, "html.parser")
    if len(soup.findAll(text=re.compile(search))) > 0:
    	myfile.write(urls[0] + "\n")
    print urls[0]

    urls.pop(0)

    for tag in soup.findAll('a', href = True):
        tag['href'] = urlparse.urljoin(url, tag['href'])
        if tag['href'] not in visited: #url in tag['href'] and 
        	urls.append(tag['href'])
        	visited.append(tag['href'])
'''
