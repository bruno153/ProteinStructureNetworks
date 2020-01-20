#PLOT A  BUNCH OF CHARTS

import numpy as np
import matplotlib.pyplot as plt

#AQUIRE FILE NAME
print "Insert file name:"
name = raw_input()
text = open((name + ".txt"), "r")
print "Enter number of models:"
datanumber = int(raw_input())

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

#IS MEAN ACTUALLY WORKING PER SNAPSHOT??
for model in range(0, datanumber):
	#GET MEAN AND STDDEV
	snap = []
	for amino in range(size):
		snap.append(betfinal[amino][model])
	mean = np.mean(snap)
	stddev = np.std(snap)
	for amino in range(size):
		zscore[amino].append((betfinal[amino][model] - mean)/stddev)

#FIND YSCALE
maxy = 0
miny = 0
for v in zscore:
	if max(v) > maxy:
		maxy = max(v)
	if min(v) < miny:
		miny = min(v)

n_groups = datanumber

fig, ax = plt.subplots()

index = np.arange(n_groups)

for i in range(0, len(betfinal)):
	plt.xlabel('Time')
	plt.ylabel('Betweenness Zscore')
	plt.title('Betweenness Zscore in function of time of amino acid ' + str(i))
	plt.legend()
	rects1 = plt.plot(index, zscore[i])
	plt.ylim([miny, maxy])
	plt.tight_layout()
	plt.savefig(name+"_charts/"+str(i)+".png")
	plt.close()
