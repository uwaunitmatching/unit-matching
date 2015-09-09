#
#class to model a unit
#author : Adrian Sasse
#
import re
import MySQLdb

class Unit:

    #constructor
    
    def __init__(self, url, code):
        print("        unit webpage is " + str(url))
        self.unitpage = url
        print("        unit code is " + str(code).upper())
        self.unitcode = code
        self.description = ""
        self.school = "NULL"
        
    #Title    
        
    def addTitle(self, title):
        print("        unit title is " + title)
        self.title = title
        
    #Description
        
    def addDescription(self, unitDesc):
        self.description = self.description + unitDesc
    
    #Add entry to database TODO
    def checkInfo(self):
        if (self.description == ""):
            self.description = "NULL"
    
    def insertUnit(self):
        print("        unit description is " + self.description)
        print("    adding unit to database")
        self.checkInfo()
        database = MySQLdb.Connect("localhost","cheese","cheese","exchange_info")
        cursor = database.cursor()
        sql = "        INSERT INTO unitlist VALUES (NULL, " + self.school + ", \'" + self.unitcode + "\', \'" + self.unitpage + "\', \'" + self.title + "\', \'" + re.escape(self.description) + "\', NULL, NULL, NULL, NULL)"
        try:
            print(sql)
            cursor.execute(sql)
            database.commit()
        except:
            print("error")
            database.rollback()
        
        