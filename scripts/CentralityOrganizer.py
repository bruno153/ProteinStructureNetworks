#Sorts the Protein____.txt output file by residue

import numpy as np
import matplotlib.pyplot as plt

#AQUIRE FILE NAME
print "Insert file name:"
name = raw_input()
text = open((name + ".txt"), "r")
print "Enter number of models:"
datanumber = int(raw_input())
print "Enter the sequence offset:"
offset = int(raw_input())

out = open((name + "_byResidue.txt"), "w")

title = text.readline()
title = title + " " + text.readline()

size = int(text.readline().split(" ")[1])

betfinal = []
zscore = []
for i in range(0, size):
	betfinal.append([])
	zscore.append([])
for j in range(0, datanumber):
	for i in range(0, size):
		s = text.readline().split(" ")[2]
		betfinal[i].append(float(s))
	text.readline()
	text.readline()
	text.readline()

for residue in range(len(betfinal)):
	#print "Residue ",residue+offset
	out.write("Residue " + str(residue+offset) + "\n")
	list = betfinal[residue]
	for i in range(len(list)):
		print (i+1), " - ", list[i]
		out.write(str(i+1) + " - " + str(list[i]) + "\n")

out.close()



