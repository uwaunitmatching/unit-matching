import csv
import sys
import re

file = sys.argv[-1]
start = None

def hasNoNumbers(inputString):
	return any(char.isalpha() for char in inputString)


with open('qsranking.csv', 'w', newline='', encoding='utf-8') as fp:
	writer = csv.writer(fp, delimiter=',')
	
	with open(file) as f:
		rankList = [""]
		nameList = [""]
		for line in f:
			if line.strip() == "1100.0":
				next(f)
				start = True
			
			if line.strip() == "Show more ranks":
				start = False
			
			if start:
				if hasNoNumbers(line.strip()):
					splitLine = line.split("\t")
					nameList.append(splitLine[0])
				else:
					if "." in line:
						rankList.append(line.strip()[:-4])
					else:
						rankList.append(line.strip())
			
		rankList[1] = 1
		print(rankList)
		print(nameList)
		
		for x in nameList:
			data = [rankList[nameList.index(x)], x]
			writer.writerow(data)

