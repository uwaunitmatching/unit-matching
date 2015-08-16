import urllib
import urllib2
import json
from pprint import pprint

URL = "https://sentinelprojects-skyttle20.p.mashape.com/"

text = """This course provides a broad introduction to machine learning and statistical pattern recognition. Topics include: supervised learning (generative/discriminative learning, parametric/non-parametric learning, neural networks, support vector machines); unsupervised learning (clustering, dimensionality reduction, kernel methods); learning theory (bias/variance tradeoffs; VC theory; large margins); reinforcement learning and adaptive control. The course will also discuss recent applications of machine learning, such as to robotic control, data mining, autonomous navigation, bioinformatics, speech recognition, and text and web data processing.
"""

opener = urllib2.build_opener(urllib2.HTTPHandler)
params = {'text': text, 'lang': 'en', 'keywords': 1}
headers = {"X-Mashape-Key": "6hQAjtFVBxmshPH0BU8zWagw4yPPp1MfGoFjsn5xQNBbxhy2Ki"}

request = urllib2.Request(URL, urllib.urlencode(params), headers=headers)
response = opener.open(request)
opener.close()
data = json.loads(response.read())

pprint(data)