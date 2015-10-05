import rake
import operator
import sys
import csv

def acceptBlobText(text):
	rake_object = rake.Rake("SmartStopList.txt", 5,2,1)
	keywords = rake_object.run(text)

	result = ""
	for keyword in keywords[0:(len(keywords) / 3)]:
		result = result + keyword[0] + ","
	#adding another one without the comma
	result = result + keywords[len(keywords)/3 + 1][0]

	return result



print acceptBlobText("This unit introduces the language structures and techniques needed to write well-structured programs in the object-oriented paradigm using the Java programming language. In particular, the process of developing appropriate classes, objects and methods to solve simple computational problems underlies the entire unit. Core computer programming topics such as the use of variables, primitive and reference data types, expressions, control structures involving selection and repetition, method decomposition and parameter passing are all covered in this context. Algorithmic techniques such as iteration, sorting, searching along with programming practices such as error handling, testing, debugging and documentation are introduced. The unit also covers advanced topics such as association, inheritance and interface. A strong focus is placed on the practical application of these concepts and techniques to produce working programs in computer laboratories. The rationale for using the object-oriented paradigm, and in particular the language Java, is covered in detail. No prior knowledge of computing or programming is assumed.")