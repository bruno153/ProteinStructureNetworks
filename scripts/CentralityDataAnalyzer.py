# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

print "Insert file name:"
name = raw_input()
text = open((name + ".txt"), "r")

out = open((name + "_sorted.txt"), "w")

number = []
centrality = []

def doublesorter(list1, list2):
	for i in range(1, len(list1)):
		j = i
		while j > 0 and list1[j]>list1[j-1]:
			list1[j], list1[j-1] = list1[j-1], list1[j]
			list2[j], list2[j-1] = list2[j-1], list2[j]
			j -= 1
	return list1, list2


#THROW AWAY THE FIRST THREE LINES
text.readline()
text.readline()
text.readline()

for line in text:
	#if line == "":
	#	break
	words = line.split()
	number.append(int(words[0]))
	centrality.append(float(words[2]))

std = np.std(centrality)
mean = np.mean(centrality)

centrality = [(i - mean)/std for i in centrality]

centrality, number = doublesorter(centrality, number)

for i in range(0, len(centrality)):
	out.write(str(number[i]) + " - " + str(centrality[i])+"\n")

x = np.linspace(0, len(centrality), len(centrality))

plt.bar(x, centrality)
plt.ylabel("z-score da centralidade")
plt.xlabel("Ordem do resíduo".encode('utf-8'))

plt.show()
