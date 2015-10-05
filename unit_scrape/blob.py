import rake
import operator
import sys
import csv

def acceptBlobText(text):
	rake_object = rake.Rake("SmartStopList.txt", 5,2,1)
	keywords = rake_object.run(text)

	result = ""
	sl = round(keywords.__len__() / 3) 
	for keyword in keywords[0:sl]:
		result = result + keyword[0] + ","
	#adding another one without the comma
	result = result + str(keywords[sl][0])

	return result