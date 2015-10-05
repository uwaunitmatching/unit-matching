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


out = open('output_keywords.txt', 'w+')


for j in range(0, len(desc)):
	# print "%d. description: %s" % (j, desc[j])
	print "ID: %s\n" % desc.keys()[j]
	keywords = rake_object.run(desc.values()[j])
	out.write('ID: %s\n' % desc.keys()[j])
	for keyword in keywords[0:(len(keywords) / 3)]:
		# for k in keyword[0].split(" "):
		# 	print "keyword: ", k
		# 	out.write('%s\n' % k)
		print "keyword: ", keyword[0]
		out.write('%s,' % keyword[0])
	out.write("%s\n" % keywords[len(keywords) / 3][0])



out.close()

