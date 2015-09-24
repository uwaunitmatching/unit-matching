#
#class to model a unit
#author : Adrian Sasse
#
import re
import MySQLdb
import DBconfig

class Unit:

    #constructor
    
    def __init__(self, url):
        self.set_url(url)
        self.description = ""
        self.school = "181"
    
    def set_url(self, url):
        print("        unit webpage is " + url)
        self.unit_page = url
        
    def add_unitcode(self, unit):
        print("        unit code is " + unit)
        self.unitcode = unit
    
    #Title    
        
    def add_title(self, title):
        print("        unit title is " + title)
        self.title = title
        
    #Description
        
    def add_description(self, unitDesc):
        self.description = self.description + unitDesc
    
    #Add entry to database 
    def checkInfo(self):
        if (self.description == ""):
            self.description = "NULL"
    
    def insertUnit(self):
        print("        unit description is " + self.description)
        print("    adding unit to database")
        sql = "        INSERT INTO unit_list VALUES (NULL, " + self.school + ", \'" + self.unitcode  + "\', \'" + self.title + "\', \'" + re.escape(self.description) + "\', NULL, NULL, NULL, NULL" + ", \'" + self.unit_page + "\')"
        print(sql)
        self.checkInfo()

#        try:
#            database = MySQLdb.Connect(DBconfig.getIP(), DBconfig.getUser(), DBconfig.getPW(), DBconfig.getDBname() )
#            cursor = database.cursor()
#        except:
#            print("Error connecting\n")
#        

#        try:
#            cursor.execute(sql)
#            database.commit()
#        except:
#            print("error!!\n")
#        database.close();
        