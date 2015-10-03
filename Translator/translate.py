import goslate
import urllib
import re

#Written by Mitchell Poole

#Needs better Language detection
def translateHTML(webpage):
	reader = webpage.read().decode(encoding='UTF-8')
	findLang = re.compile('lang="([a-z][a-z])" ', re.IGNORECASE)
	lang = re.findall(findLang,reader)
	print("FINDING")
	#print(lang[0])

	if(lang[0] == 'en'):
		return webpage
	else:
		gs = goslate.Goslate(goslate.WRITING_NATIVE,timeout=30)
		print("TRANSLATING...")
		trans = gs.translate(reader, 'en', source_language=lang[0]) #LOOK UP AND SEE IF ENCODING ISSUE
		return trans



page = urllib.request.urlopen('http://el.wikipedia.org/')


second = urllib.request.urlopen('http://en.wikipedia.org/wiki/Main_Page')
#print(second.read())
#print(second)

#Prints correct html
#print(string.decode(encoding='UTF-8'))

f = translateHTML(page)
