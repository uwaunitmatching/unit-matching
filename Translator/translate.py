import goslate
import urllib
import re

#Written by Mitchell Poole
#Changed it to open the URL within the function and have the function return a string
def translateHTML(url):
	reader = urllib.request.urlopen(url).read().decode(encoding='UTF-8')
	findLang = re.compile('lang="([a-z][a-z])" ', re.IGNORECASE)
	lang = re.findall(findLang,reader)
	print("FINDING")

	#Don't bother if page is already English
	if(lang[0] == 'en'):
		return webpage
	else:
		gs = goslate.Goslate(goslate.WRITING_NATIVE,timeout=30)
		print("TRANSLATING...")
		if lang[0] is not None:
			trans = gs.translate(reader, 'en', source_language=lang[0]) 
		else: #If the language can't be found
			trans = gs.translate(reader, 'en')	
		return trans
