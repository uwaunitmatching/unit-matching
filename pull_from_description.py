import MySQLdb as mdb
import sys
import skyttle-client


URL = "https://sentinelprojects-skyttle20.p.mashape.com/"

# pull from column 'unit_desc' in table 'unitlist'

con = mdb.connect('localhost', 'root', '', 'exchange_database');

textarray = []

with con: 

    cur = con.cursor()
    cur.execute("SELECT unit_desc FROM unitlist")

    rows = cur.fetchall()

    for row in rows:
        #print row
        textarray.append(row)



print "test: "
print textarray
print get_keywords_from_api(textarray[1])
