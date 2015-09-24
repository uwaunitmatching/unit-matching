#
#recursive functions to scrape web-site
#author : Adrian Sasse
#


from urllib.request import urlopen
from urllib.error import  URLError
import handleHTML
from Stack import Stack


#urls already visited
visited = set()
#urls to visit
stack = Stack()
#parser object to manipulate HTML
parser = handleHTML.parse()
parser.re_init(stack, visited)


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
        file = urlopen(url)
    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
    else:
        visited.add(url)
        parser.setUnitFalse()
        buildUnit(url, file)

#construct a table entry from unit web-page HTML
    
def buildUnit(url, file):
    parser.setUnitFalse()
    visited.add(url)
    parser.set_url(url)
    for line in file:
        parser.feed(line.decode('utf8'))
    if parser.isUnit:
        parser.unit.insertUnit()   
    
#TODO
    
def loadText():        
    exit(-1)
    