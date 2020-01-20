# Software designed to calculate covariance of 
# centralities on molecular dynamics simulations.
#
# Input: Protein(centrality).py output file
# Output: List of covariance on CMD

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

cov = np.cov(betfinal, ddof=0)

covList = []
pairList = []

for i in range(0, size):
	for j in range(i + 1, size):
		covList.append(cov[i][j])
		pairList.append(str(i + offset) + " " + str(j + offset))

#apply zscore
#covList = sp.zscore(covList)


for i in range(0, len(covList)):
	print pairList[i], " ", covList[i]