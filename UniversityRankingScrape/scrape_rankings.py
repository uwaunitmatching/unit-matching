#! /usr/bin/python
import re
import urllib
import csv
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

#webpage = urllib.request.urlopen('https://www.timeshighereducation.com/world-university-rankings/2016/world-ranking#!/page/1/length/-1')

# Using default python html parser for compatibility within systems





soup = BeautifulSoup(open("html.txt"), "html.parser")

table= soup.find("table", { "id" : "datatable-1"} )
rows = table.findAll("tr")

# File is opened using utf-8 as is handles all characters

with open('timesranking.csv', 'w', newline='', encoding='utf-8') as fp:
	writer = csv.writer(fp, delimiter=',')
	i = 0
	for row in rows:
		print(row)
		cells = row.findAll("td" )
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
					print(rank)
				elif j == 1:
					name = cell.find('a').get_text()
					print(name)
				#elif j == 2:
				#	country = cell.get_text().strip()
				#elif j == 3:
				#	region = cell.get_text().strip()
				j = j + 1
		i = i + 1
		data = [rank, name]
		writer.writerow(data)
