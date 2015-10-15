
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import DBconfig
import html.parser
import re


def insert_uni(db, name, city, country, region, proper):
        print (name + ", " + city + ", " + country + ", " + region + ", " + proper)
        sql = "INSERT INTO app_university VALUES (NULL, \'" + name + "\', \'" + city + "\', \'" + country + "\', \'" + region + "\', NULL, \'" + proper + "\')"
        try:
            database = pymysql.connect(db.getIP(), db.getUser(), db.getPW(), db.getDBname() )
            cursor = database.cursor()
            try:
                    cursor.execute(sql)
            except:
                    print("sql error")   
            database.commit()
            database.close();
            print("Insertion Success")
        except:
            print("Error connecting\n")
        

def get_proper_link(initlink ):
	portal_string = "http://www.globalstudio.uwa.edu.au/"
	portal_string += initlink

	page = urlopen(portal_string)
	soup = BeautifulSoup(page)

	homepage = soup.find('a', {"title" : "Click to visit the homepage"})['href']
	return homepage


def downUnis(db, zipo):

        webpage = urlopen('http://www.globalstudio.uwa.edu.au/index.cfm?FuseAction=Programs.SearchResults&Program_Name=&Program_Type_ID=1&pi=%7F&pc=%7F&pr=%7F&pt=%7F&Partner_ID=ANY&p_10003=%7F&p_10003_t=MULTI&p_10004=%7F&p_10004_t=MULTI&p_10005=%7F&p_10005_t=MULTI&p_10008=Exchange+Program%7F&p_10008_t=SELCT&p_10009=%7F&p_10009_t=MULTI&Sort=Program_Name&Order=asc&pp=10003%2C10004%2C10005%2C10008%2C10009')


        soup = BeautifulSoup(webpage, "html.parser")

        table= soup.find("table", { "class" : "bot-bdr"} )
        rows = table.findAll("tr")

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
                if (i != 0):
                        for cell in cells:
                                if (j == 0):
                                        name = cell.get_text().strip()
                                if (len(name.split('  (not')) == 2):
                                        name = name.split('  (not')[0]
                                elif(j == 1):
                                        city = cell.get_text().strip()
                                elif(j == 2):
                                        country = cell.get_text().strip()
                                elif(j == 3):
                                        region = cell.get_text().strip()
                                j+=1
                        insert_uni(db, name, city, country, region, proper)
                i = i + 1
                
                
