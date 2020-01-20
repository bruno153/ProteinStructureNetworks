# Software designed to calculate closeness centrality
# of amino acid residues in a protein structure provided 
# by a pdb file. It is now intended for single or 
# multiple protein structures uses.
#
# Input: protein strucutre in pdb file
# Output: Closeness list in txt file
#         Event log in txt file
#
# python ProteinCloseness.py
# Insert file name:
# 4dc2_no_substrate
# Done Model
# Done LOL

#NO CHAIN LIST PRESENT


import Graph
distLim = 5
aminomaxsize = 30

def isOnList(list, x):
    for i in list:
        if i == x:
            return True
    return False

#AQUIRE FILE NAME
print "Insert file name (without _graph.txt):"
name = raw_input()

out = open((name + "_betweenness.txt"), "w")

text = open((name + "_graph.txt"), "r")

log = open((name + "_log.txt"), "w")

resseq = []
tag = ""
line = " "

title = ""
model = ""
size = 0

aminoList = []
atomList = []

#present amino acid numbers list
chainList = []
nameList = []
first = True


while True:
    #FOR EVERY PROTEIN MODEL
    line = text.readline()
    #WHILE THE FILE HAS NOT ENDED
    if line == "":
        break

    for i in range(3):
        #AQUIRE TAG
        tag = line.split(" ")[0]
        #remove whitespace
        tag.replace("\n", "")
        
        #INTERPRET TAG
        if tag == "TITLE":
            title = line[10:]
        if tag == "MODEL":
            model = int(line[6:])
        if tag == "SIZE":
        	size = int(line[5:])

        line = text.readline()
    aminoList.append(atomList)
    out.write("TITLE " + title)
    out.write("MODEL " + str(model) + "\n")
    out.write("SIZE " + str(size) + "\n")

    #START THE CONTACT MATRIX
    graph = Graph.Graph(size)
    
    tag = line.split(" ")[0]
    print line
    while not(tag.find("END") > -1) :
    	line = line.split(" ")
    	i = int(line[0])
    	j = int(line[1])
    	graph.addEdge(i, j)

    	line = text.readline()
    	tag = line.split(" ")[0]
    

    bet = Graph.Betweenness(graph)
    betList = bet.getBet()
    for i in range(0, graph.size()):
        out.write(str(chainList[i]) + " - " + str(betList[i]) + "\n")


    print "Done Model " + str(model)
    #RESET EVERYTHING
    title = ""
    model = ""
    tag = ""
    aminoList = []
    atomList = []
    #throw away the end line
    text.readline()
print "Done"