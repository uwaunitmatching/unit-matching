import rake
import operator
import sys
import csv

rake_object = rake.Rake("SmartStopList.txt", 5, 2, 1)




names = {}
desc = {}
i = 0

f = open('units.csv', 'r')

try:
	reader = csv.reader(f, delimiter=',')
	for row in reader:
		if not row[1] == "NULL" or not row[2] == "NULL":
			names[row[0]] = row[1]
			desc[row[0]] = row[2]

		i+=1

finally:
	f.close()


for j in range(1,20):
	# print "%d. description: %s" % (j, desc[j])
	print "ID: %s" % desc.keys()[j]
	keywords = rake_object.run(desc.values()[j])
	print "Keywords:", keywords



