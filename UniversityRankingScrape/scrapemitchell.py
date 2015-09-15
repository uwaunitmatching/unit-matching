#! /usr/bin/python
import re
import urllib
import csv
from html2text import html2text

from bs4 import BeautifulSoup




def get_proper_link(initlink ):
	portal_string = "http://www.globalstudio.uwa.edu.au/"
	portal_string += initlink

	page = urllib.request.urlopen(portal_string)
	soup = BeautifulSoup(page)

	homepage = soup.find('a', {"title" : "Click to visit the homepage"})['href']
	return homepage




webpage = urllib.request.urlopen('http://www.globalstudio.uwa.edu.au/index.cfm?FuseAction=Programs.SearchResults&Program_Name=&Program_Type_ID=1&pi=%7F&pc=%7F&pr=%7F&pt=%7F&Partner_ID=ANY&p_10003=%7F&p_10003_t=MULTI&p_10004=%7F&p_10004_t=MULTI&p_10005=%7F&p_10005_t=MULTI&p_10008=Exchange+Program%7F&p_10008_t=SELCT&p_10009=%7F&p_10009_t=MULTI&Sort=Program_Name&Order=asc&pp=10003%2C10004%2C10005%2C10008%2C10009')


soup = BeautifulSoup(webpage)

table= soup.find("table", { "class" : "bot-bdr"} )
rows = table.findAll("tr")

with open('out.csv', 'w', newline='') as fp:
	writer = csv.writer(fp, delimiter=',')
	i = 0
	for row in rows:
		cells = row.findAll("td")
		link = ""
		proper = ""
		if i != 0:
			link = row.find('a', href=True)['href']
			proper = get_proper_link(link)
		name = ""
		city = ""
		country = ""
		region = ""

		j = 0

		if i != 0:
			for cell in cells:
				if j == 0:
					name = cell.get_text().strip()
				elif j == 1:
					city = cell.get_text().strip()
				elif j == 2:
					country = cell.get_text().strip()
				elif j == 3:
					region = cell.get_text().strip()
				j = j + 1
		i = i + 1
		data = [name, city, country, region, proper]
		writer.writerow(data)
		print(link, name, city, country, region)
