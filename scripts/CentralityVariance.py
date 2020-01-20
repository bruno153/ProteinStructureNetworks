# This software is designed to scatter plot
# and illustrate de relationship between
# mean centrality and variance, it is 
# supposed that betweennes tend to
# oscillate a lot on central residues,
# whereas closeness not as much.
#
# Input: Protein(CENTRALITY).py centrality list txt file
# Output: Scatter plot on the tks.


import numpy as np
import matplotlib.pyplot as plt

print "Insert file name:"
name = raw_input()
text = open((name + ".txt"), "r")
outMean = open((name + "_mean.txt"), "w")
outVar = open((name + "_var.txt"), "w")

text.readline()
text.readline()
size = int(text.readline().split()[1])
print "Size = ", size

cent = [[] for i in range(size)]
number = []

for i in range(size):
    line = text.readline().split()
    number.append(int(line[0]))
    cent[i].append(float(line[2]))

while line != "":
    text.readline()
    text.readline()
    line = text.readline()
    if line == "":
        break
    for i in range(size):
        line = text.readline().split()
        cent[i].append(float(line[2]))

variance = []
mean = []

for i in cent:
    mean.append(np.mean(i))
    variance.append(np.var(i))
 

for i in range(len(mean)):
    outMean.write(str(number[i])+" "+str(mean[i])+ "\n")
    outVar.write(str(number[i])+" "+str(variance[i])+ "\n")


plt.scatter(mean,variance)
plt.show()

