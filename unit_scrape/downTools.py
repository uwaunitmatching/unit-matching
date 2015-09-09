#
#recursive functions to scrape web-site
#author : Adrian Sasse
#


from urllib.request import urlopen
from urllib.error import  URLError
import handleHTML
from Stack import Stack
from Unit import Unit
import re

#urls already visited
visited = set()
#urls to visit
stack = Stack()
#parser object to manipulate HTML
parser = handleHTML.parse()
parser.re_init(stack, visited)
#regex to match a unit in URL
unitregex = re.compile("[a-z]{3,5}[0-9]{3,5}", re.IGNORECASE)

#recursively load URL via stack

def recursiveload(url, dom):
    count = 0
    stack.push(url)
    while stack.isEmpty() != True:
        try:
            newurl = stack.pop()
            if dom in newurl:
                if newurl not in visited:
                    count = count + 1 
                    loadUrl(newurl, count)
        except:
            print("error in " + newurl)
            continue
                
#load a single URL

def loadUrl(url, count):
    print("[" + str(count) + "]" + "attempting to scrape " + url)
       
    try:
        f = urlopen(url)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        if unitregex.search(url):
            code = unitregex.search(url)
            print("Unit Found!! building unit data")
            parser.setUnitTrue()
            buildUnit(url, code.group(0),f)
        else:
            parser.setUnitFalse()
            for line in f:
                parser.feed(line.decode('utf8'))
                visited.add(url)
        f.close()

#construct a table entry from unit web-page HTML
    
def buildUnit(url, code, file):
    thisUnit = Unit(url, code)
    visited.add(url)
    parser.set_unit(thisUnit)
    for line in file:
        parser.feed(line.decode('utf8'))
    thisUnit.insertUnit()   
    
#TODO
    
def loadText():        
    exit(-1)
    