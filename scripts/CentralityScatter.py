# Software designed to scatter plot centralities of
# pairs.
#
# Input: Protein(centrality).py output file
# Output: Plots on CMD

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

#AQUIRE FILE NAME
print "Insert file name:"
name = raw_input()
text = open((name + ".txt"), "r")
print "Enter number of models:"
datanumber = int(raw_input())
print "Enter offset:"
offset = int(raw_input())

title = text.readline()
title = title + " " + text.readline()

size = int(text.readline().split(" ")[1])

betfinal = []
for i in range(0, size):
	betfinal.append([])
for j in range(0, datanumber):
	for i in range(0, size):
		s = text.readline().split(" ")[2]
		betfinal[i].append(float(s))
	text.readline()
	text.readline()
	text.readline()

while True:
	print "Insert x axis residue:"
	i = int(raw_input()) - 22
	print "Insert y axis residue:"
	j = int(raw_input()) - 22
	plt.scatter(betfinal[i], betfinal[j])
	plt.show()