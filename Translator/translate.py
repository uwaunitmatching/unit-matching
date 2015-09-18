import goslate
import urllib
from bs4 import BeautifulSoup

def translate(webpage):
	soup = BeautifulSoup(webpage, "html.parser")
	language = soup.find('lang')#, lang=True)['lang']
	if language != 'en' or language is None:
		go = goslate.Goslate()
		translated = go.translate(webpage, 'en')

		return translated
	else:
		return webpage



url = 'http://de.wikipedia.org/wiki/Wikipedia:Hauptseite'


page = urllib.request.urlopen(url)


soup = BeautifulSoup(page, "html.parser")

trans = translate(page)

print(trans)
