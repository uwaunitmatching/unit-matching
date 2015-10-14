#
#Storage for the database connection information !!NOT TO BE PUSHED TO PUBLIC GIT
#author Adrian Sasse
#

#connection details for database goes here



class DBconfig:

    

    def __init__(self):
        self.ipordomain = ""
        self.username = "" 
        self.password = ""
        self.databasename = ""

    def getIP(self):
        return self.ipordomain
        
    def getUser(self):
        return self.username

    def getPW(self):
        return self.password
        
    def getDBname(self):
        return self.databasename
        
    def setIP(self, string):
        self.ipordomain = string
        
    def setUser(self, string):
        self.username = string

    def setPW(self, string):
        self.password = string

    def setDBname(self, string):
        self.databasename = string
