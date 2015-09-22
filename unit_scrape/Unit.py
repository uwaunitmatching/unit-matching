#
#class to model a unit
#author : Adrian Sasse
#
import re
import MySQLdb
import DBconfig

class Unit:

    #constructor
    
    def __init__(self, url, code):
        print("        unit webpage is " + str(url))
        self.unitpage = url
        print("        unit code is " + str(code).upper())
        self.unitcode = code
        self.description = ""
        self.school = "181"
        
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
        sql = "        INSERT INTO unit_list VALUES (NULL, " + self.school + ", \'" + self.unitcode  + "\', \'" + self.title + "\', \'" + re.escape(self.description) + "\', NULL, NULL, NULL, NULL" + ", \'" + self.unitpage + "\')"
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
        