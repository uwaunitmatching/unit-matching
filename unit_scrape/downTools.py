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
in_stack = set()
#parser object to manipulate HTML
parser = handleHTML.parse()
#parser.re_init(stack, visited, in_stack)


#recursively load URL via stack

def recursiveload(url, dom, db):
    database = db
    count = 0
    stack.push(url)
    in_stack.add(url)
    while stack.isEmpty() != True:
        try:
            newurl = stack.pop()
            in_stack.remove(newurl)
            if dom in newurl:
                if newurl not in visited:
                    count = count + 1 
                    loadUrl(newurl, count, database)
        except:
            print("error in " + newurl)
            continue
                
#load a single URL

def loadUrl(url, count, db):
    database = db
    print("[" + str(count) + "]" + "[" + str(stack.size()) + "]" + "attempting to scrape " + url)
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
        buildUnit(url, file, database)

#construct a table entry from unit web-page HTML
    
def buildUnit(url, file, db):
    database = db
    parser.setUnitFalse()
    visited.add(url)
    parser.re_init(stack, visited, in_stack, database)
    parser.set_url(url)
    for line in file:
        parser.feed(line.decode('utf8'))
    if parser.isUnit:
        parser.unit.insertUnit()   
    
#TODO
    
def loadText():        
    exit(-1)
    
