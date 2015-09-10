import MySQLdb as mdb
import sys
import skyttle_client
import json

con = mdb.connect('localhost', 'root', '', 'exchange_database');
textarray = []
unit_key_array = []
unit_code_array = []
results = []


# pull from column 'unit_desc' in table 'unitlist'
def pull_from_desc():
	with con: 

	    cur = con.cursor()
	    cur.execute("SELECT unit_desc FROM unitlist")

	    rows_desc = cur.fetchall()

	    for row in rows_desc:
	        textarray.append(row)

	    cur.execute("SELECT unit_code FROM unitlist")

	    rows_code = cur.fetchall()

	    for row in rows_code:
	        unit_code_array.append(row)
	        # print "code: " + repr(row)

	    cur.execute("SELECT unit_key FROM unitlist")

	    rows_keys = cur.fetchall()

	    for row in rows_keys:
	        unit_key_array.append(row)
	      	# print "key: " + repr(row)

	return textarray;


def save_into_keywords():
	desc_array = pull_from_desc()

	# print unit_key_array
	# print unit_code_array

	for i in range(0, len(desc_array)):
		jsondata = json.loads(skyttle_client.get_keywords_from_api(desc_array[i]))['docs'][0]['terms']
		# print i
		result = ""

		for j in range(0, len(jsondata)):
			# print j
			result = result + str(jsondata[j]['term']).lower() + ','

		results.append(result)

	cursor = con.cursor()

	add_keywords = ("INSERT INTO unitkeywords "
	               "(unit_key, unit_code, unit_desc)"
	               "VALUES (%s, %s, %s)")
	

	print results
	numrows = len(results)

	for i in range(0, numrows):
		# print "this i = " + repr(i)
		# every unit key, unit code

		data_entry = (unit_key_array[i], unit_code_array[i], results[i])
		cursor.execute(add_keywords, data_entry)
	
	# emp_no = cursor.lastrowid

	# Make sure data is committed to the database
	con.commit()

	cursor.close()






save_into_keywords()
con.close()
