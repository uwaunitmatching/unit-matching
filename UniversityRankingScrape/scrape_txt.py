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
					name = splitLine[0]
					nameLength = len(name)
					splitLength = int(nameLength / 2)
					if nameLength % 2 == 0 and name[:splitLength] == name[-splitLength:]:
						nameList.append(name[:splitLength])
					else :
						nameList.append(name)
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

