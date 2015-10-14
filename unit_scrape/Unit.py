#
#class to model a unit
#author : Adrian Sasse
#
import re
import pymysql
import DBconfig
import blob

class Unit:

    #constructor
    
    def __init__(self, url, db):
        self.db = db
        self.set_url(url)
        self.unitcode = ""
        self.title = ""
        self.description = ""
        self.school = "50"
    
    def set_url(self, url):
        self.unit_page = url
        
    def add_unitcode(self, unit):
        print("        unit webpage is " + self.unit_page, flush=True)
        print("        unit code is " + unit, flush=True)
        self.unitcode = unit
    
    #Title    
        
    def add_title(self, title):
        print("        unit title is " + title, flush=True)
        self.title = title
        
    #Description
        
    def add_description(self, unitDesc):
        self.description = self.description + unitDesc + " "
    
    def extract_keywords(self):
        self.keywords = blob.acceptBlobText(self.description) 
        print("        unit keywords are: " +  self.keywords , flush=True)
        
    #Add entry to database 
    def checkInfo(self):
        if (self.unitcode == ""):
            self.unitcode = "NULL"
        if (self.school == ""):
            self.school = "NULL"
        if (self.title == ""):
            self.title = "NULL"
        if (self.description == ""):
            self.description = "NULL"
            self.keywords = "NULL"
            return False
        else:
            return True
    
    def insertUnit(self):
        result = self.checkInfo()
        if (result):
            self.extract_keywords()
        print("        unit description found!", flush=True)
        print("    adding unit to database", flush=True)
        self.checkInfo()
        self.sql = "INSERT INTO app_units VALUES (NULL, " + self.school + ", \'" + self.unitcode  + "\', \'" + self.title + "\', \'" + re.escape(self.description) + "\' , NULL, NULL, \'" + re.escape(self.keywords) + "\', NULL" + ", \'" + self.unit_page  + "\')"

        try:
            database = pymysql.connect(self.db.getIP(), self.db.getUser(), self.db.getPW(), self.db.getDBname() )
            cursor = database.cursor()
        except:
            print("Error connecting\n")
       
        try:
            cursor.execute(self.sql)
            database.commit()
        except:
            print("error!!\n")
        database.close();
