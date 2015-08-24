import urllib
import urllib2
import json
from pprint import pprint

URL = "https://sentinelprojects-skyttle20.p.mashape.com/"

def get_keywords_from_api(bigstring):

	text = bigstring

	opener = urllib2.build_opener(urllib2.HTTPHandler)
	params = {'text': text, 'lang': 'en', 'keywords': 1}
	headers = {"X-Mashape-Key": "6hQAjtFVBxmshPH0BU8zWagw4yPPp1MfGoFjsn5xQNBbxhy2Ki"}

	request = urllib2.Request(URL, urllib.urlencode(params), headers=headers)
	response = opener.open(request)
	opener.close()



	data = response.read()

	return data;


