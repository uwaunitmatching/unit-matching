#! /usr/bin/python
import re
import urllib
import csv
from html2text import html2text
import sys

from bs4 import BeautifulSoup

#def get_proper_link(initlink ):
#	portal_string = "http://www.globalstudio.uwa.edu.au/"
#	portal_string += initlink
#
#	page = urllib.request.urlopen(portal_string)
#	soup = BeautifulSoup(page)
#
#	homepage = soup.find('a', {"title" : "Click to visit the homepage"})['href']
#	return homepage

webpage = urllib.request.urlopen('http://www.shanghairanking.com/ARWU2015.html')

# Using default python html parser for compatibility within systems

soup = BeautifulSoup(webpage, "html.parser")

table= soup.find("table", { "id" : "UniversityRanking"} )
rows = table.findAll("tr")

# File is opened using utf-8 as it handles all characters

with open('shanghairanking.csv', 'w', newline='', encoding='utf-8') as fp:
	writer = csv.writer(fp, delimiter=',')
	i = 0
	for row in rows:
		cells = row.findAll("td")
		#link = ""
		#proper = ""
		#if i != 0:
                        #link = row.find('a', href=True)['href']
			#proper = get_proper_link(link)
		rank = ""
		name = ""

		j = 0

		if i != 0:
			for cell in cells:
				if j == 0:
					rank = cell.get_text().strip()
				elif j == 1:
					name = cell.get_text().strip().split("\n")[0]
				#elif j == 2:
				#	country = cell.get_text().strip()
				#elif j == 3:
				#	region = cell.get_text().strip()
				j = j + 1
		i = i + 1
		data = [rank, name]
		writer.writerow(data)
		print(rank, name)
