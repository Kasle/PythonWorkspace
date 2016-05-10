import urlparse
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
            soup = BeautifulSoup(htmltext, "html.parser")
            if len(soup.findAll(text=re.compile(search))) > 0:
                myfile.write(urls[0] + "\n")

            urls.pop(0)

            for tag in soup.findAll('a', href = True):
                tag['href'] = urlparse.urljoin(url, tag['href'])
                if tag['href'] not in visited: #url in tag['href'] and
                    urls.append(tag['href'])
                    visited.append(tag['href'])
        except:
            pass
