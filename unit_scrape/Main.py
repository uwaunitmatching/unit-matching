#
#base script gathers arguments see --help
#author : Adrian Sasse
#

#build in functions
import argparse
import re

#my functions
import downTools



parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="enter a single unit to be scraped (http://...)\n")
parser.add_argument("-r", "--recurse_url", help="enter a URL to recursively scrape\n")
parser.add_argument("-t", "--text_file", help="enter a text file containing the list of unit webpages to scrape (*.txt)\n")
args = parser.parse_args()

#regex to check type of input given
a = re.compile("^http", re.IGNORECASE)
b = re.compile("\\.txt$", re.IGNORECASE)

#recursive url load
if args.recurse_url and a.match(args.recurse_url):
    dom = args.recurse_url.split('/')[2]
    print("current domain is " + dom)
    downTools.recursiveload(args.recurse_url, dom)   

#single url load
elif args.url and a.match(args.url):
    dom = args.url.split('/')[2]
    print("current domain is " + dom)
    downTools.loadUrl(args.url, 0)  

#textfile url load
elif args.text_file and b.match(args.text_file):
    print("Loading url's from " + args.text_file + "\n")
    downTools.loadText(args.text_file)

else:
    print("Invalid input, see --help\n")

#find domain

   
#scan domain until all sites visited
