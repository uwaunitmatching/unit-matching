import rake
import operator
import sys
import csv

def acceptBlobText(text):
	rake_object = rake.Rake("SmartStopList.txt", 5,2,1)
	keywords = rake_object.run(text)

	result = ""
	for keyword in keywords[0:(len(keywords) / 3)]:
		result = result + keyword + ","
	#adding another one without the comma
	result = result + keywords[len(keywords)/3]

	return result