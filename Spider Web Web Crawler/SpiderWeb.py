
import urlparse
import urllib
from bs4 import BeautifulSoup

#https://en.wikipedia.org/wiki/Special:Random
url = 'http://hyperphysics.phy-astr.gsu.edu'
#url = raw_input("Web Seed: ")

search = raw_input('Please enter search term(s) seperated by commas: ').split(",")

urls = [url] #Current URLs
visited = [url] #Historic URLs

_br = False

blackfile = open('blacklist.txt','r')
blacklist = blackfile.readlines()
blackfile.close()

#print blacklist

def checkPass(que):
    for i in blacklist:
#        print "checkPass:", i.strip() in que
        if i.strip() in que:
            return False
    return True
    
def AinB(A, B):
    for i in A:
#        print "Testing:",i.strip()
        if i.strip() not in B:
#            print False
            return False
#    print True
    return True

while len(urls) > 0:
    try:
        print "Current:",len(urls),urls[0]
        htmltext = urllib.urlopen(urls[0]).read()
        soup = BeautifulSoup(htmltext, "html.parser")
        if AinB(search, soup.get_text()):
            myfile = open("results.txt", "a")
            myfile.write(", ".join(search) + " : " + urls[0] + "\n")
            myfile.close()
        
#        print urls[0] not in visited    
        
        if urls[0] not in visited:
            visited.append(urls.pop(0))
        else:
            urls.pop(0)
            
        for tag in soup.findAll('a', href = True):
            tag['href'] = urlparse.urljoin(url, tag['href'])
#            print tag['href'], len(urls)
#            print tag['href'] not in visited, checkPass(tag['href'])
            if tag['href'] not in visited and checkPass(tag['href']): #url in tag['href'] and
                urls.append(tag['href'])
    except:
        print "ERROR: Blacklisting",urls[0]
        blackfile = open('blacklist.txt',"a")
        blackfile.write(urls[0]+"\n")
        blackfile.close()
        blackfile = open('blacklist.txt', 'r')
        blacklist = blackfile.readlines()
        blackfile.close()
        visited.append(urls.pop(0))
        pass
    