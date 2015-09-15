# Load CSV data into MySQL in Python

import csv
import pymysql
import codecs

def csv_unireader(f, encoding="utf-8"):
    for row in csv.reader(codecs.iterencode(codecs.iterdecode(f, encoding), "utf-8")):
        yield [e.decode("utf-8") for e in row]

conn = pymysql.connect(host='localhost', user='root', passwd='ravinoramrod7267',
db='unitmatching')
cursor = conn.cursor()

f = open('timesranking.csv', newline='', encoding='utf-8')
csv_data = csv.reader(f)
for row in csv_data:

    cursor.execute('INSERT INTO universitylist("(first_name, last_name, hire_date, gender, birth_date) "
               "VALUES (%s, %s, %s, %s, %s)")
#close the connection to the database.
conn.commit()
cursor.close()
print("Done")
