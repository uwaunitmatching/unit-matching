import MySQLdb as mdb
import sys
import skyttle_client
import json


# pull from column 'unit_desc' in table 'unitlist'
def pull_from_desc():

	con = mdb.connect('localhost', 'root', '', 'exchange_database');

	textarray = []

	with con: 

	    cur = con.cursor()
	    cur.execute("SELECT unit_desc FROM unitlist")

	    rows = cur.fetchall()

	    for row in rows:
	        #print row
	        textarray.append(row)

	return textarray;


def save_into_keywords():

	desc_array = pull_from_desc()

	for i in range(0, len(desc_array)):
		jsondata = json.loads(skyttle_client.get_keywords_from_api(desc_array[i]))['docs'][0]['terms']
	
		for j in range(0, len(jsondata)):
			results = jsondata[j]['term']
			print results
		print "Number of keywords: %d" % (j,)


save_into_keywords()